from pathlib import Path

import openai

from ..utils import get_logger
from .exchange import usd_to_gbp

logger = get_logger(__name__)


class Whisper:
    _PRICE_DOLLARS_PER_SECOND = 0.006 / 60
    _MODEL = "whisper-1"

    def get_price_pounds(self, seconds: float) -> float:
        dollars = seconds * self._PRICE_DOLLARS_PER_SECOND
        gbp = usd_to_gbp(dollars)
        pence = gbp * 100
        logger.info(f"Estimated transcription cost: {pence:.2f}p")
        return gbp

    def __call__(self, path: Path) -> str:
        with open(path, "rb") as f:
            transcript = openai.Audio.transcribe(  # type: ignore[no-untyped-call]
                self._MODEL,
                f,
                language="es",
            )
        assert isinstance(transcript.text, str)
        return transcript.text
