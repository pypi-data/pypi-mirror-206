from typing import Dict, TypeVar, TypeAlias, Generic, Iterable, Optional

TKey = TypeVar("TKey")
TValue = TypeVar("TValue")

Tree: TypeAlias = TValue | Dict[TKey, TValue] | Dict[TKey, "Tree[TKey, TValue]"]


class DictItemBase(Generic[TKey, TValue]):
    def __init__(self, source: Tree[TKey, TValue], allow_new_keys: bool = False) -> None:
        self.source = source
        self.allow_new_keys = allow_new_keys

    def get(self, path: TKey, default: TValue | None = None) -> Tree | None:
        try:
            return self[path]
        except KeyError:
            return default

    def __getitem__(self, path: TKey) -> Tree | KeyError:
        item = self.source
        for key in self._split(path):
            item = item[key]  # type: ignore
        return item

    def __setitem__(self, path: TKey, value: TValue):
        item: Tree = self.source
        *head, tail = self._split(path)
        keys: list[TKey] = []
        for key in head:
            keys.append(key)
            try:
                item = item[key]
                if not isinstance(item, dict):
                    raise ItemNotDict(f"Path: {self._join(keys)}.")
            except KeyError:
                if not self.allow_new_keys:
                    raise KeyNotFound(f"Path: {self._join(keys)}.")
                item[key] = item = {}
        item[tail] = value

    def _split(self, path: TKey) -> Iterable[TKey]:
        raise NotImplementedError(f"{self.__class__.__name__}._split has not been defined")

    def _join(self, path: Iterable[TKey]) -> TKey:
        raise NotImplementedError(f"{self.__class__.__name__}._join has not been defined")


class KeyNotFound(Exception):
    pass


class ItemNotDict(Exception):
    pass


class DictItem(DictItemBase[str, TValue]):
    """Gets or sets an item at the specified path consisting of multiple keys."""

    def __init__(self, source: Tree[str, TValue], allow_new_keys: bool = False, separator: str = "/"):
        super().__init__(source, allow_new_keys)
        self.separator = separator

    def _split(self, path: str) -> Iterable[str]:
        return path.split(self.separator)

    def _join(self, path: Iterable[str]) -> str:
        return self.separator.join(path)
