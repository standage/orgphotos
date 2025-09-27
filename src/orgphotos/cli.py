# This file is part of orgphotos (https://github.com/standage/orgphotos).
# (c) Daniel Standage, 2025.

from argparse import ArgumentParser
from .sorter import PhotoSorter
from pathlib import Path
from pillow_heif import register_heif_opener
from rich_argparse import RichHelpFormatter
from tqdm import tqdm


def driver(arglist=None):
    if arglist:
        arglist = map(str, arglist)
    args = get_parser().parse_args(arglist)
    main(args.indir, args.outdir)


def main(indir, outdir):
    register_heif_opener()
    sorter = PhotoSorter.new(outdir)
    infiles = tqdm(list(Path(indir).glob("*")))
    sorter.sort(infiles)
    print("\n[Sorted images]")
    for extension, count in sorter.sort_count.most_common():
        print(f"{extension}\t{count}")
    print("\n[Unsorted images/other files]")
    for extension, count in sorter.triage_count.most_common():
        print(f"{extension}\t{count}")


def get_parser():
    parser = ArgumentParser(formatter_class=RichHelpFormatter)
    parser.add_argument("indir", help="input directory")
    parser.add_argument("outdir", help="output directory")
    parser.add_argument(
        "-d",
        "--dryrun",
        action="store_true",
        help="don't copy photos, just show what would have been done",
    )
    return parser
