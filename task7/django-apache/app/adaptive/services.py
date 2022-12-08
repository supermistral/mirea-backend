from pathlib import Path
from typing import List, Optional

from django.conf import settings
from django.core.files.uploadedfile import UploadedFile

from .utils import save_file, get_files_in_dir


def save_file_by_session_id(session_id: str, file: UploadedFile) -> None:
    path = Path(settings.SESSION_FILES_ROOT, session_id, file.name)
    return save_file(path, file)


def get_file_by_session_id(session_id: str, filename: str) -> Optional[Path]:
    path = Path(settings.SESSION_FILES_ROOT, session_id, filename)
    return path if path.is_file() else None


def get_files_by_session_id(session_id: str) -> List[str]:
    folder = Path(settings.SESSION_FILES_ROOT, session_id)
    return get_files_in_dir(folder)
