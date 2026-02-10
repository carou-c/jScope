from PySide6.QtWidgets import QToolBar
from PySide6.QtGui import QAction

from ..core.controller import Controller

class MainToolBar(QToolBar):
    def __init__(self, controller: Controller):
        super().__init__()

        self.controller: Controller = controller

        refresh_action = QAction("Refresh", self)
        refresh_action.triggered.connect(controller.refresh)

        self.addAction(refresh_action)
