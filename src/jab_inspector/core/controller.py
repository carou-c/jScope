from typing import Iterable
from PySide6.QtCore import QObject, Signal, QThread

from ..core.models import AccessibleNode
from ..core.backend import AccessibilityBackend

class RefreshWorker(QObject):
    finished = Signal()

    def __init__(self, backend: AccessibilityBackend):
        super().__init__()
        self.backend = backend

    def run(self):
        self.backend.refresh()
        self.finished.emit()

class Controller(QObject):
    node_selected = Signal(object)
    tree_loaded = Signal()
    status_message = Signal(str, int)

    def __init__(self, backend: AccessibilityBackend):
        super().__init__()
        self.backend = backend

    def roots(self) -> Iterable[AccessibleNode]:
        return self.backend.get_root_nodes()

    def select_node(self, node: AccessibleNode):
        self.node_selected.emit(node)
        self.highlight(node)

    def highlight(self, node: AccessibleNode):
        self.backend.highlight(node)

    def reload_tree(self):
        self.status_message.emit("Loading Accessbility Tree...", 0)

        self._thread = QThread()
        self._worker = RefreshWorker(self.backend)
        self._worker.moveToThread(self._thread)
        self._thread.started.connect(self._worker.run)
        self._worker.finished.connect(self._on_tree_reload)
        self._worker.finished.connect(self._thread.quit)

        self._thread.finished.connect(self._thread.deleteLater)
        self._worker.finished.connect(self._worker.deleteLater)

        self._thread.start()

    def _on_tree_reload(self):
        self.tree_loaded.emit()
        self.node_selected.emit(None)
        self.status_message.emit("Accessibility Tree Loaded", 0)
