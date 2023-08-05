# Copyright (c) 2022-2023 Mario S. Könz; License: MIT
import os
import typing as tp  # pylint: disable=reimported
from pathlib import _posix_flavour  # type: ignore
from pathlib import _windows_flavour  # type: ignore
from pathlib import Path

from django.core.files.storage import get_storage_class

# 2023-Q1: sphinx has a bug regarding adjusting the signature for attributes,
# hence I need fully qualified imports for typing and django.db

__all__ = ["DjangoPath"]


class DjangoPath(Path):
    _flavour = _windows_flavour if os.name == "nt" else _posix_flavour

    def name_wo_prefix(self) -> str:
        name = self.as_posix()
        print(f"\033[1;32m========>> {hasattr(self, 'prefix')} {self}\033[0m")

        if self._prefix:  # type: ignore
            name = name.split(self._prefix + "/", 1)[1]  # type: ignore
        return name

    @classmethod
    def create(cls, path: Path | str, prefix: str | None) -> "DjangoPath":
        # pylint: disable=attribute-defined-outside-init
        res = cls(path)
        res._prefix = prefix  # type: ignore
        return res

    def __copy__(self) -> "DjangoPath":
        # pylint: disable=protected-access,no-member,attribute-defined-outside-init
        res = self.__class__(self)
        res._prefix = self._prefix  # type: ignore
        return res

    def __deepcopy__(self, memo: dict[tp.Any, tp.Any]) -> "DjangoPath":
        # pylint: disable=protected-access,no-member,attribute-defined-outside-init
        res = self.__class__(self)
        res._prefix = self._prefix  # type: ignore
        return res

    def open(  # type: ignore  # pylint: disable=too-many-arguments
        self,
        mode: str = "r",
        buffering: int = -1,
        encoding: str | None = None,
        errors: str | None = None,
        newline: str | None = None,
    ) -> tp.IO[tp.Any]:
        # assert encoding is None
        assert errors is None
        assert newline is None
        assert buffering == -1
        media_storage = get_storage_class()()
        return media_storage.open(self.as_posix(), mode=mode)
