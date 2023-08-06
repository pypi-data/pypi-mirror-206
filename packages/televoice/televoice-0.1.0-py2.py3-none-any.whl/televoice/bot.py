import datetime
import os
import tempfile
import time
from pathlib import Path

import openai
from pydub import AudioSegment
from telegram import Update
from telegram import Voice
from telegram.ext import ApplicationBuilder
from telegram.ext import ContextTypes
from telegram.ext import MessageHandler
from telegram.ext import filters

from .apis import Whisper
from .utils import get_cache_dir
from .utils import get_logger

logger = get_logger(__name__)


class Bot:
    def __init__(self) -> None:
        logger.info("Initializing bot")
        self._transcriber = Whisper()
        telegram_token = os.environ["TELEVOICE_BOT_TOKEN"]
        self._application = ApplicationBuilder().token(telegram_token).build()
        self._add_handlers()
        self._cache_dir = get_cache_dir()
        self._show_cost = False

    def _add_handlers(self) -> None:
        voice_handler = MessageHandler(filters.VOICE, self._voice_callback)
        self._application.add_handler(voice_handler)

    async def _send(self, message: str) -> None:
        assert self.update.effective_chat is not None
        await self.context.bot.send_message(
            chat_id=self.update.effective_chat.id,
            text=message,
        )

    def _set_update_context(
        self,
        update: Update,
        context: ContextTypes.DEFAULT_TYPE,
    ) -> None:
        self.update = update
        self.context = context

    async def _check_is_me(self) -> bool:
        my_client_id = int(os.environ["TELEGRAM_CLIENT_ID"])
        assert self.update.effective_chat is not None
        is_me = self.update.effective_chat.id == my_client_id
        if is_me:
            return True
        else:
            await self._send("Sorry, I'm not allowed to chat with you.")
            return False

    async def _get_mp3_from_voice(self, voice: Voice) -> Path:
        voice_file = await voice.get_file()
        time_string = datetime.datetime.now().isoformat()
        filename = f"{time_string}_voice.mp3"
        mp3_path = self._cache_dir / filename
        with tempfile.NamedTemporaryFile(suffix=".oga") as f:
            oga_path = Path(f.name)
            await voice_file.download_to_drive(oga_path)
            oga_file: AudioSegment = AudioSegment.from_file(oga_path, format="ogg")
            oga_file.export(mp3_path, format="mp3")
        logger.info(f"Saved voice message to {mp3_path}")
        logger.info(f"File size: {mp3_path.stat().st_size / 2**20:.3} MiB")
        return mp3_path

    async def _voice_callback(
        self,
        update: Update,
        context: ContextTypes.DEFAULT_TYPE,
        max_num_attempts: int = 3,
        waiting_time: float = 1,
    ) -> None:
        self._set_update_context(update, context)

        assert update.message is not None
        assert isinstance(update.message.voice, Voice)
        voice = update.message.voice
        logger.info(f"Voice message received ({voice.duration} seconds)")
        mp3_path = await self._get_mp3_from_voice(voice)

        if not await self._check_is_me():
            return

        logger.info("Transcribing audio...")
        assert update.effective_chat is not None
        await self._send(f"[Transcribing {voice.duration} seconds of audio...]")
        attempts = 0
        while attempts < max_num_attempts:
            try:
                transcript = self._transcriber(mp3_path)
                logger.info(f'Transcript: "{transcript}"')
                await self._send(transcript)
                return
            except openai.error.APIConnectionError:
                await self._send("[Transcription error. Trying again...]")
                attempts += 1
                time.sleep(waiting_time)
        await self._send("[Transcription API not working. Try using text...]")

    def run(self) -> None:
        logger.info("The bot is ready")
        self._application.run_polling()
