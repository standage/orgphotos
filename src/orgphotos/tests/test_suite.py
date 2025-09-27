# This file is part of orgphotos (https://github.com/standage/orgphotos).
# (c) Daniel Standage, 2025.

from orgphotos import cli
import pytest


def test_usage(capsys):
    with pytest.raises(SystemExit):
        cli.driver(["--help"])
    terminal = capsys.readouterr()
    assert "-d, --dryrun" in terminal.out
