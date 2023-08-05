# Stubs for selector
# See https://docs.python.org/3/library/selectors.html

from typing import Any, List, NamedTuple, Mapping, Tuple, Optional, Union
from abc import ABCMeta, abstractmethod
import socket


# Type aliases added mainly to preserve some context
#
# See https://github.com/python/typeshed/issues/482
# for details regarding how _FileObject is typed.
_FileObject = Union[int, socket.socket]
_FileDescriptor = int
_EventMask = int


EVENT_READ: _EventMask
EVENT_WRITE: _EventMask


SelectorKey = NamedTuple('SelectorKey', [
    ('fileobj', _FileObject),
    ('fd', _FileDescriptor),
    ('events', _EventMask),
    ('data', Any)
])


class BaseSelector(metaclass=ABCMeta):
    @abstractmethod
    def register(self, fileobj: _FileObject, events: _EventMask, data: Any = ...) -> SelectorKey: ...

    @abstractmethod
    def unregister(self, fileobj: _FileObject) -> SelectorKey: ...

    def modify(self, fileobj: _FileObject, events: _EventMask, data: Any = ...) -> SelectorKey: ...

    @abstractmethod
    def select(self, timeout: Optional[float] = ...) -> List[Tuple[SelectorKey, _EventMask]]: ...

    def close(self) -> None: ...

    def get_key(self, fileobj: _FileObject) -> SelectorKey: ...

    @abstractmethod
    def get_map(self) -> Mapping[_FileObject, SelectorKey]: ...

    def __enter__(self) -> BaseSelector: ...

    def __exit__(self, *args: Any) -> None: ...

class SelectSelector(BaseSelector):
    def register(self, fileobj: _FileObject, events: _EventMask, data: Any = ...) -> SelectorKey: ...
    def unregister(self, fileobj: _FileObject) -> SelectorKey: ...
    def select(self, timeout: Optional[float] = ...) -> List[Tuple[SelectorKey, _EventMask]]: ...
    def get_map(self) -> Mapping[_FileObject, SelectorKey]: ...

class PollSelector(BaseSelector):
    def register(self, fileobj: _FileObject, events: _EventMask, data: Any = ...) -> SelectorKey: ...
    def unregister(self, fileobj: _FileObject) -> SelectorKey: ...
    def select(self, timeout: Optional[float] = ...) -> List[Tuple[SelectorKey, _EventMask]]: ...
    def get_map(self) -> Mapping[_FileObject, SelectorKey]: ...

class EpollSelector(BaseSelector):
    def fileno(self) -> int: ...
    def register(self, fileobj: _FileObject, events: _EventMask, data: Any = ...) -> SelectorKey: ...
    def unregister(self, fileobj: _FileObject) -> SelectorKey: ...
    def select(self, timeout: Optional[float] = ...) -> List[Tuple[SelectorKey, _EventMask]]: ...
    def get_map(self) -> Mapping[_FileObject, SelectorKey]: ...

class DevpollSelector(BaseSelector):
    def fileno(self) -> int: ...
    def register(self, fileobj: _FileObject, events: _EventMask, data: Any = ...) -> SelectorKey: ...
    def unregister(self, fileobj: _FileObject) -> SelectorKey: ...
    def select(self, timeout: Optional[float] = ...) -> List[Tuple[SelectorKey, _EventMask]]: ...
    def get_map(self) -> Mapping[_FileObject, SelectorKey]: ...

class KqueueSelector(BaseSelector):
    def fileno(self) -> int: ...
    def register(self, fileobj: _FileObject, events: _EventMask, data: Any = ...) -> SelectorKey: ...
    def unregister(self, fileobj: _FileObject) -> SelectorKey: ...
    def select(self, timeout: Optional[float] = ...) -> List[Tuple[SelectorKey, _EventMask]]: ...
    def get_map(self) -> Mapping[_FileObject, SelectorKey]: ...

class DefaultSelector(BaseSelector):
    def register(self, fileobj: _FileObject, events: _EventMask, data: Any = ...) -> SelectorKey: ...
    def unregister(self, fileobj: _FileObject) -> SelectorKey: ...
    def select(self, timeout: Optional[float] = ...) -> List[Tuple[SelectorKey, _EventMask]]: ...
    def get_map(self) -> Mapping[_FileObject, SelectorKey]: ...
