from _typeshed import Incomplete
from ctypes import CDLL
from pyjab.accessibleinfo import AccessBridgeVersionInfo as AccessBridgeVersionInfo, AccessibleActions as AccessibleActions, AccessibleActionsToDo as AccessibleActionsToDo, AccessibleContextInfo as AccessibleContextInfo, AccessibleKeyBindings as AccessibleKeyBindings, AccessibleRelationSetInfo as AccessibleRelationSetInfo, AccessibleTableCellInfo as AccessibleTableCellInfo, AccessibleTableInfo as AccessibleTableInfo, AccessibleTextAttributesInfo as AccessibleTextAttributesInfo, AccessibleTextInfo as AccessibleTextInfo, AccessibleTextItemsInfo as AccessibleTextItemsInfo, AccessibleTextRectInfo as AccessibleTextRectInfo, AccessibleTextSelectionInfo as AccessibleTextSelectionInfo, VisibleChildrenInfo as VisibleChildrenInfo
from pyjab.common.logger import Logger as Logger
from pyjab.common.types import JOBJECT64 as JOBJECT64

class JABFixedFunc:
    log: Incomplete
    bridge: Incomplete
    def __init__(self, bridge: CDLL) -> None: ...
