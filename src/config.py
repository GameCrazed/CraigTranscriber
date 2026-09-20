from __future__ import annotations

import os
from pathlib import Path
from dotenv import load_dotenv

load_dotenv()

BASE_DIR = Path(__file__).resolve().parent.parent
INPUT_ZIPS_DIR = BASE_DIR / "input_zips"
EXTRACTED_DIR = BASE_DIR / "extracted"
OUTPUTS_DIR = BASE_DIR / "outputs"
TEMP_CHUNKS_DIR = BASE_DIR / "temp_chunks"

INPUT_ZIPS_DIR.mkdir(parents=True, exist_ok=True)
EXTRACTED_DIR.mkdir(parents=True, exist_ok=True)
OUTPUTS_DIR.mkdir(parents=True, exist_ok=True)
TEMP_CHUNKS_DIR.mkdir(parents=True, exist_ok=True)

WHISPER_MODELS_DIR = Path(os.getenv("WHISPER_MODELS_DIR", r"C:\Whisper Models"))

def _resolve_model_path() -> Path:
    env_val = os.getenv("WHISPER_MODEL_PATH", "").strip()
    if env_val:
        return Path(env_val)
    candidates = sorted(WHISPER_MODELS_DIR.glob("*.bin"))
    if not candidates:
        raise FileNotFoundError(
            f"No ggml .bin model found in {WHISPER_MODELS_DIR}. "
            "Download a model (e.g. ggml-base.en.bin) and place it there, "
            "or set WHISPER_MODEL_PATH in your .env file."
        )
    return candidates[0]

WHISPER_MODEL_PATH = _resolve_model_path()

SUPPORTED_AUDIO_EXTENSIONS = {
    ".flac",
    ".wav",
    ".ogg",
    ".mp3",
    ".aac",
    ".m4a",
    ".mp4",
    ".webm",
    ".opus",
}

MIN_SILENCE_LEN_MS = 1200
SILENCE_THRESH_OFFSET_DB = 16
KEEP_SILENCE_MS = 250
MAX_CHUNK_MS = 30000
MIN_CHUNK_MS = 800