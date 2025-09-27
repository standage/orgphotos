# This file is part of orgphotos (https://github.com/standage/orgphotos).
# (c) Daniel Standage, 2025.

from .image import ImageFile
from collections import Counter
from dataclasses import dataclass
from pathlib import Path
from PIL import UnidentifiedImageError
from shutil import copy


@dataclass
class PhotoSorter:
    outdir: Path
    sort_count: Counter
    triage_count: Counter
    mock: bool = True

    @classmethod
    def new(cls, outdir):
        return cls(Path(outdir), Counter(), Counter())

    def sort(self, infiles):
        for infile in infiles:
            try:
                image = ImageFile.from_path(infile)
                if image.has_date:
                    self.sort_image_by_date(image)
                else:
                    self.triage_file(image)
            except UnidentifiedImageError:
                self.triage_file(image)

    def sort_image_by_date(self, image):
        self.sort_count[image.extension] += 1
        month_dir = self.outdir / image.year / image.month
        if not self.mock:
            month_dir.mkdir(parents=True, exist_ok=True)
            copy(image.path, month_dir / image.path.name)

    def triage_file(self, image):
        unsorted_dir = self.outdir / "unsorted"
        unsorted_dir.mkdir(parents=True, exist_ok=True)
        copy(image.path, unsorted_dir / image.path.name)
        self.triage_count[image.extension] += 1
