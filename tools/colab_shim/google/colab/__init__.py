"""로컬용 google.colab 대체 모듈 (Colab 전용 API를 로컬에서 동작하도록 흉내 냄)."""
from . import drive, files, output, patches

__all__ = ["drive", "files", "output", "patches"]
