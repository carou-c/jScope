from PySide6.QtWidgets import QMainWindow, QSplitter
from PySide6.QtCore import Qt

from ..core.controller import Controller
from ..ui.tree_panel import TreePanel
from ..ui.property_panel import PropertyPanel
from ..ui.toolbar import MainToolBar


class InspectorWindow(QMainWindow):
    def __init__(self, controller: Controller):
        super().__init__()

        self.setWindowTitle("JAB Inspector")
        self.resize(1200, 800)

        toolbar = MainToolBar(self, controller)
        self.addToolBar(toolbar)

        splitter = QSplitter(Qt.Orientation.Horizontal, parent=self)

        tree = TreePanel(splitter, controller)
        props = PropertyPanel(splitter)

        splitter.addWidget(tree)
        splitter.addWidget(props)

        splitter.setStretchFactor(0, 1)
        splitter.setStretchFactor(1, 2)

        self.setCentralWidget(splitter)

        status = self.statusBar()

        controller.node_selected.connect(props.display_node)
        controller.tree_loaded.connect(tree.rebuild)
        controller.status_message.connect(status.showMessage)

        controller.reload_tree()
