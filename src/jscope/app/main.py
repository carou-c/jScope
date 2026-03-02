import sys
from argparse import ArgumentParser

from PySide6.QtWidgets import QApplication

from ..core.controller import Controller
from ..app.window import InspectorWindow


def main():
    arg_parser = ArgumentParser(
        "jScope", description="Inspector tool for Java desktop applications"
    )
    arg_parser.add_argument(
        "--backend",
        "-b",
        required=True,
        help="Backend to use. Must be 'mock' or 'pyjab'.",
    )
    arg_parser.add_argument(
        "--bridge-dll",
        "-dll",
        required=False,
        help="Path to the Java Access Bridge dll.",
    )
    arg_parser.add_argument(
        "--window-title", "-w", required=False, help="Title of window to be inspected"
    )

    args = arg_parser.parse_args()

    match args.backend:
        case "mock":
            from ..backends.mock import MockBackend
            backend = MockBackend()
        case "pyjab":
            from pyjab.jabdriver import JABDriver
            from ..backends.pyjab import PyjabBackend

            if (args.window_title is None) or (args.bridge_dll is None):
                raise ValueError(
                    "pyjab backend requires '--bridge-dll' and '--window-title' CLI arguments."
                )
            jabdriver = JABDriver(title=args.window_title, bridge_dll=args.bridge_dll)
            backend = PyjabBackend(jabdriver)
        case _:
            raise ValueError(f"Backend {args.backend!r} is invalid.")

    app = QApplication(sys.argv)

    controller = Controller(backend)

    win = InspectorWindow(controller)
    win.show()

    sys.exit(app.exec())


if __name__ == "__main__":
    main()
