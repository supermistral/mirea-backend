import datetime
from typing import Any, Dict, List, Optional
from pathlib import Path

from django.conf import settings


def get_filename_from_fields(name1: Optional[str], name2: Optional[str]) -> str:
    """
    Returns file name where name1 takes precedence over name2
    """
    filename = name1 if name1 is not None else name2
    assert filename is not None

    return filename


def get_stats_images() -> List[str]:
    """
    Parses statistics directory and returns .png images
    """
    images_globs = Path(settings.STATS_MEDIA_ROOT).glob('*.png')
    base_images_url = Path('/' + settings.STATS_MEDIA_URL)
    return sorted([str(base_images_url / x.name) for x in images_globs])


def datetime_parser(dictionary: Dict[Any, Any]) -> Dict[Any, Any]:
    for k, v in dictionary.items():
        if 'date' in k:
            dictionary[k] = datetime.datetime.strptime(v, '%Y-%m-%d').date()
    return dictionary
