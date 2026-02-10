from PySide6.QtWidgets import QMainWindow, QSplitter
from PySide6.QtCore import Qt

from ..core.controller import Controller
from ..ui.tree_panel import TreePanel
from ..ui.property_panel import PropertyPanel


class InspectorWindow(QMainWindow):
    def __init__(self, controller: Controller):
        super().__init__()

        self.setWindowTitle("JAB Inspector")
        self.resize(1200, 800)

        splitter = QSplitter(Qt.Orientation.Horizontal)

        self.tree = TreePanel(controller)
        self.props = PropertyPanel()

        splitter.addWidget(self.tree)
        splitter.addWidget(self.props)

        splitter.setStretchFactor(0, 1)
        splitter.setStretchFactor(1, 2)

        self.setCentralWidget(splitter)

        controller.node_selected.connect(self.props.display_node)
