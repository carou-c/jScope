from ..core.models import AccessibleRole, AccessibleState, AccessibleNode, Bounds


class MockBackend:
    def __init__(self):
        self.root = AccessibleNode(
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
            parent=None,
            children=[
                AccessibleNode(
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
                    parent=None,
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

    def get_root_nodes(self):
        return [self.root]

    def refresh(self):
        print("Refreshed")

    def highlight(self, node: AccessibleNode):
        print("Highlight: ", node)
