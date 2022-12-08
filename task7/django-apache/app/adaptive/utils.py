from pathlib import Path
from typing import List

from django.core.files.uploadedfile import UploadedFile


def save_file(path: str, file: UploadedFile) -> None:
    output = Path(path)
    output.parent.mkdir(parents=True, exist_ok=True)

    with open(output, 'wb+') as f:
        for chunk in file.chunks():
            f.write(chunk)


def get_files_in_dir(path: Path) -> List[str]:
    if path.is_dir():
        return [f.name for f in path.iterdir() if f.is_file()]
    return []
