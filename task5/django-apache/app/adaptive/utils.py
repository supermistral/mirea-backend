from pathlib import Path
from typing import Dict, List, Optional

from django.conf import settings
from django.core.files.uploadedfile import UploadedFile


def save_file(path: str, file: UploadedFile) -> None:
    output = Path(path)
    output.parent.mkdir(parents=True, exist_ok=True)

    with open(output, 'wb+') as f:
        for chunk in file.chunks():
            f.write(chunk)


def save_file_by_session_id(session_id: str, file: UploadedFile) -> None:
    path = Path(settings.MEDIA_ROOT, session_id, file.name)
    return save_file(path, file)


def get_file_by_session_id(session_id: str, filename: str) -> Optional[Path]:
    path = Path(settings.MEDIA_ROOT, session_id, filename)
    print(path)
    return path if path.is_file() else None


def get_files_by_session_id(session_id: str) -> List[str]:
    folder = Path(settings.MEDIA_ROOT, session_id)

    if folder.is_dir():
        return [f.name 
                for f in folder.iterdir()
                if f.is_file()]
    return []
