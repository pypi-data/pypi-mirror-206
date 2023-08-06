# This file is part of lsst-resources.
#
# Developed for the LSST Data Management System.
# This product includes software developed by the LSST Project
# (https://www.lsst.org).
# See the COPYRIGHT file at the top-level directory of this distribution
# for details of code ownership.
#
# Use of this source code is governed by a 3-clause BSD-style
# license that can be found in the LICENSE file.

from __future__ import annotations

import contextlib
import logging
import re
import sys

if sys.version_info >= (3, 11, 0):
    from importlib import resources
else:
    import importlib_resources as resources  # type: ignore[no-redef]

from typing import Iterator

__all__ = ("PackageResourcePath",)

from ._resourceHandles._baseResourceHandle import ResourceHandleProtocol
from ._resourcePath import ResourcePath

log = logging.getLogger(__name__)


class PackageResourcePath(ResourcePath):
    """URI referring to a Python package resource.

    These URIs look like: ``resource://lsst.daf.butler/configs/file.yaml``
    where the network location is the Python package and the path is the
    resource name.
    """

    def exists(self) -> bool:
        """Check that the python resource exists."""
        ref = resources.files(self.netloc).joinpath(self.relativeToPathRoot)
        return ref.is_file() or ref.is_dir()

    def read(self, size: int = -1) -> bytes:
        """Read the contents of the resource."""
        ref = resources.files(self.netloc).joinpath(self.relativeToPathRoot)
        with ref.open("rb") as fh:
            return fh.read(size)

    @contextlib.contextmanager
    def open(
        self,
        mode: str = "r",
        *,
        encoding: str | None = None,
        prefer_file_temporary: bool = False,
    ) -> Iterator[ResourceHandleProtocol]:
        # Docstring inherited.
        if "r" not in mode or "+" in mode:
            raise RuntimeError(f"Package resource URI {self} is read-only.")
        ref = resources.files(self.netloc).joinpath(self.relativeToPathRoot)
        with ref.open(mode, encoding=encoding) as buffer:
            yield buffer

    def walk(
        self, file_filter: str | re.Pattern | None = None
    ) -> Iterator[list | tuple[ResourcePath, list[str], list[str]]]:
        # Docstring inherited.
        if not self.dirLike:
            raise ValueError("Can not walk a non-directory URI")

        if isinstance(file_filter, str):
            file_filter = re.compile(file_filter)

        ref = resources.files(self.netloc).joinpath(self.relativeToPathRoot)

        files: list[str] = []
        dirs: list[str] = []
        for item in ref.iterdir():
            if item.is_file():
                files.append(item.name)
            else:
                # This is a directory.
                dirs.append(item.name)

        if file_filter is not None:
            files = [f for f in files if file_filter.search(f)]

        if not dirs and not files:
            return
        else:
            yield type(self)(self, forceAbsolute=False, forceDirectory=True), dirs, files

        for dir in dirs:
            new_uri = self.join(dir, forceDirectory=True)
            yield from new_uri.walk(file_filter)
