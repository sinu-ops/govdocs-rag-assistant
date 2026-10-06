import os
from pathlib import Path


PROJECT_ROOT = Path(__file__).resolve().parent.parent

DATA_PATH = Path(os.getenv("GOVDOCS_DATA_PATH") or PROJECT_ROOT / "data" / "raw")

QDRANT_PATH = Path(os.getenv("GOVDOCS_QDRANT_PATH") or PROJECT_ROOT / "qdrant_db")

ENV_PATH = PROJECT_ROOT / ".env"
