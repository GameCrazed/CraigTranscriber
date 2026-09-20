from __future__ import annotations

from pathlib import Path

from pywhispercpp.model import Model

from config import WHISPER_MODEL_PATH


_model = Model(str(WHISPER_MODEL_PATH))


def transcribe_file(audio_path: Path) -> str:
    segments = _model.transcribe(str(audio_path))
    return " ".join(seg.text for seg in segments).strip()