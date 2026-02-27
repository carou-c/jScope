from time import sleep
from ..core.models import AccessibleRole, AccessibleState, AccessibleNode, Bounds


class MockBackend:
    def __init__(self):
        self.root = AccessibleNode(
            id=0,
            name="Demo App",
            description="Demo Application",
            role=AccessibleRole.FRAME,
            states={
                AccessibleState.ENABLED,
                AccessibleState.FOCUSABLE,
                AccessibleState.VISIBLE,
                AccessibleState.SHOWING,
                AccessibleState.FOCUSED,
                AccessibleState.ACTIVE,
            },
            bounds=Bounds(0, 0, 800, 600),
            object_depth=0,
            index_in_parent=-1,
            parent_id=None,
            children=[
                AccessibleNode(
                    id=1,
                    name="Submit",
                    description="Submit Button",
                    role=AccessibleRole.PUSH_BUTTON,
                    states={
                        AccessibleState.ENABLED,
                        AccessibleState.FOCUSABLE,
                        AccessibleState.VISIBLE,
                        AccessibleState.SHOWING,
                    },
                    bounds=Bounds(50, 50, 120, 40),
                    object_depth=1,
                    index_in_parent=0,
                    parent_id=0,
                    children=[],
                    supports_acc_component=True,
                    supports_acc_action=True,
                    supports_acc_selection=False,
                    supports_acc_text=False,
                )
            ],
            supports_acc_component=True,
            supports_acc_action=False,
            supports_acc_selection=False,
            supports_acc_text=False,
        )

        self.__nodes: list[AccessibleNode] = [
            self.root,
            self.root.children[0]
        ]

    def get_root_nodes(self):
        return [self.root]

    def refresh(self):
        sleep(2)

    def highlight(self, node: AccessibleNode):
        print("Highlight: ", node)
