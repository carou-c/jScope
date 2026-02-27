from enum import Enum

class States(str, Enum):
    BUSY = 'busy'
    CHECKED = 'checked'
    ENABLED = 'enabled'
    FOCUSED = 'focused'
    SELECTED = 'selected'
    PRESSED = 'pressed'
    EXPANDED = 'expanded'
    COLLAPSED = 'collapsed'
    ICONIFIED = 'iconified'
    MODAL = 'modal'
    MULTI_LINE = 'multi_line'
    FOCUSABLE = 'focusable'
    EDITABLE = 'editable'
    VISIBLE = 'visible'
    SHOWING = 'showing'
    UNKNOWN = 'unknown'
