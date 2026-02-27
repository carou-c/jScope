from abc import abstractmethod
from typing import Protocol, Iterable

from .models import AccessibleNode


class AccessibilityBackend(Protocol):
    __nodes: list[AccessibleNode]

    def get_root_nodes(self) -> Iterable[AccessibleNode]:
        return [
            node for node in self.__nodes
            if node.parent_id is None
        ]

    @abstractmethod
    def refresh(self) -> None: ...

    @abstractmethod
    def highlight(self, node: AccessibleNode) -> None: ...
