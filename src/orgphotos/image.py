# This file is part of orgphotos (https://github.com/standage/orgphotos).
# (c) Daniel Standage, 2025.

from calendar import month_name
from dataclasses import dataclass
from pathlib import Path
from PIL import Image, ExifTags
from typing import Dict


@dataclass
class ImageFile:
    path: Path
    image: Image
    meta: Dict

    @classmethod
    def from_path(cls, path):
        path = Path(path)
        image = Image.open(path)
        if hasattr(image, "getexif"):
            exif = {ExifTags.TAGS[k]: v for k, v in image.getexif().items() if k in ExifTags.TAGS}
        else:
            exif = {ExifTags.TAGS[k]: v for k, v in image._getexif().items() if k in ExifTags.TAGS}
        return cls(path, image, exif)

    @property
    def extension(self):
        return self.path.suffix.lower()

    @property
    def has_date(self):
        return "DateTime" in self.meta

    @property
    def year(self):
        return self.meta["DateTime"].split(":")[0]

    @property
    def month(self):
        month_number = int(self.meta["DateTime"].split(":")[1])
        name = month_name[month_number]
        return f"{month_number:02d}{name}"
