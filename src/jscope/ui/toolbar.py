from PySide6.QtWidgets import QToolBar, QWidget
from PySide6.QtGui import QAction

from ..core.controller import Controller

class MainToolBar(QToolBar):
    def __init__(self, parent: QWidget | None, controller: Controller):
        super().__init__("Main", parent=parent)

        # self.controller: Controller = controller

        reload_action = QAction("Reload", self)
        reload_action.triggered.connect(controller.reload_tree)

        self.addAction(reload_action)
