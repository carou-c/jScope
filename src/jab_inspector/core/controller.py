from PySide6.QtCore import QObject, Signal

from ..core.models import AccessibleNode
from ..core.backend import AccessibilityBackend

class Controller(QObject):
    node_selected = Signal(AccessibleNode)
    tree_refreshed = Signal()

    def __init__(self, backend: AccessibilityBackend):
        super().__init__()
        self.backend = backend

    def roots(self):
        return self.backend.get_root_nodes()

    def select_node(self, node: AccessibleNode):
        self.node_selected.emit(node)

    def highlight(self, node: AccessibleNode):
        self.backend.highlight(node)

    def refresh(self):
        self.backend.refresh()
        self.tree_refreshed.emit()
        self.node_selected.emit(None)
