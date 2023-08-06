"""
Utility functions for pod5 tools
"""

import os
import typing
from pathlib import Path


PBAR_DEFAULTS = dict(ascii=True, smoothing=0.0, dynamic_ncols=True)


def iterate_inputs(
    input_items: typing.Iterable[Path], recursive: bool, file_pattern: str
) -> typing.Generator[Path, None, None]:
    """
    Returns a generator of file Paths which match the given glob-style file_pattern
    (e.g. .pod5).

    If an input item is a directory this will be globbed (optionally recursively).
    If the input item is a file then it must also match the given file_pattern.
    """
    # Get the recursive or non-recursive glob function.
    glob_fn = Path.rglob if recursive else Path.glob
    for input_item in input_items:
        if input_item.is_dir():
            for glob_path in glob_fn(input_item, file_pattern):
                if glob_path.is_file():
                    yield glob_path

        # Non-directory, assert that it is a file and that it matches the file_pattern
        elif input_item.match(file_pattern) and input_item.is_file():
            yield input_item


def is_disable_pbar() -> bool:
    """Check if POD5_PBAR is set returning true if PBAR should be disabled"""
    try:
        enabled = bool(int(os.environ.get("POD5_PBAR", "1")))
        return not enabled
    except Exception:
        return False


def is_pod5_debug() -> bool:
    """Check if POD5_DEBUG is set"""
    try:
        debug = bool(int(os.environ.get("POD5_DEBUG", "0")))
        return debug
    except Exception:
        return True
