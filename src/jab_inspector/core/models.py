from typing import Self
from enum import StrEnum, auto
from dataclasses import dataclass


class AccessibleRole(StrEnum):
    ALERT = auto()
    AWT_COMPONENT = auto()
    CANVAS = auto()
    CHECK_BOX = auto()
    COLOR_CHOOSER = auto()
    COLUMN_HEADER = auto()
    COMBO_BOX = auto()
    DATE_EDITOR = auto()
    DESKTOP_ICON = auto()
    DESKTOP_PANE = auto()
    DIALOG = auto()
    DIRECTORY_PANE = auto()
    EDITBAR = auto()
    FILE_CHOOSER = auto()
    FILLER = auto()
    FONT_CHOOSER = auto()
    FOOTER = auto()
    FRAME = auto()
    GLASS_PANE = auto()
    GROUP_BOX = auto()
    HEADER = auto()
    HTML_CONTAINER = auto()
    HYPERLINK = auto()
    ICON = auto()
    INTERNAL_FRAME = auto()
    LABEL = auto()
    LAYERED_PANE = auto()
    LIST = auto()
    LIST_ITEM = auto()
    MENU = auto()
    MENU_BAR = auto()
    MENU_ITEM = auto()
    OPTION_PANE = auto()
    PAGE_TAB = auto()
    PAGE_TAB_LIST = auto()
    PANEL = auto()
    PARAGRAPH = auto()
    PASSWORD_TEXT = auto()
    POPUP_MENU = auto()
    PROGRESS_BAR = auto()
    PROGRESS_MONITOR = auto()
    PUSH_BUTTON = auto()
    RADIO_BUTTON = auto()
    ROOT_PANE = auto()
    ROW_HEADER = auto()
    RULER = auto()
    SCROLL_BAR = auto()
    SCROLL_PANE = auto()
    SEPARATOR = auto()
    SLIDER = auto()
    SPIN_BOX = auto()
    SPLIT_PANE = auto()
    STATUS_BAR = auto()
    SWING_COMPONENT = auto()
    TABLE = auto()
    TEXT = auto()
    TOGGLE_BUTTON = auto()
    TOOL_BAR = auto()
    TOOL_TIP = auto()
    TREE = auto()
    UNKNOWN = auto()
    VIEWPORT = auto()
    WINDOW = auto()


class AccessibleState(StrEnum):
    ACTIVE = auto()
    ARMED = auto()
    BUSY = auto()
    CHECKED = auto()
    COLLAPSED = auto()
    EDITABLE = auto()
    ENABLED = auto()
    EXPANDABLE = auto()
    EXPANDED = auto()
    FOCUSABLE = auto()
    FOCUSED = auto()
    HORIZONTAL = auto()
    ICONIFIED = auto()
    INDETERMINATE = auto()
    MANAGES_DESCENDANTS = auto()
    MODAL = auto()
    MULTI_LINE = auto()
    MULTISELECTABLE = auto()
    OPAQUE = auto()
    PRESSED = auto()
    RESIZABLE = auto()
    SELECTABLE = auto()
    SELECTED = auto()
    SHOWING = auto()
    SINGLE_LINE = auto()
    TRANSIENT = auto()
    TRUNCATED = auto()
    VERTICAL = auto()
    VISIBLE = auto()


@dataclass
class Bounds:
    x: int
    y: int
    width: int
    height: int


@dataclass
class AccessibleNode:
    name: str | None
    description: str | None
    role: AccessibleRole
    states: set[AccessibleState]
    bounds: Bounds
    object_depth: int
    index_in_parent: int
    parent: Self | None
    children: list[Self]
    supports_acc_component: bool
    supports_acc_action: bool
    supports_acc_selection: bool
    supports_acc_text: bool
