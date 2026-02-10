import sys
from PySide6.QtWidgets import QApplication

from ..core.controller import Controller
from ..backends.mock import MockBackend
from ..app.window import InspectorWindow


def main():
    app = QApplication(sys.argv)

    backend = MockBackend()
    controller = Controller(backend)

    win = InspectorWindow(controller)
    win.show()

    sys.exit(app.exec())


if __name__ == "__main__":
    main()
