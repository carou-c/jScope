from PySide6.QtWidgets import QWidget, QFormLayout, QLabel

from ..core.models import AccessibleNode


class PropertyPanel(QWidget):
    def __init__(self):
        super().__init__()

        self.layout = QFormLayout(self)  # type: ignore

        self.node_name = QLabel()
        self.node_description = QLabel()
        self.node_role = QLabel()
        self.node_states = QLabel()
        self.node_bounds = QLabel()
        self.node_object_depth = QLabel()
        self.node_index_in_parent = QLabel()
        # self.node_parent = QLabel()
        # self.node_children = QLabel()
        self.node_children_count = QLabel()
        self.node_supports_acc_component = QLabel()
        self.node_supports_acc_action = QLabel()
        self.node_supports_acc_selection = QLabel()
        self.node_supports_acc_text = QLabel()

        self.layout.addRow("Role:", self.node_role)
        self.layout.addRow("Name:", self.node_name)
        self.layout.addRow("Description:", self.node_description)
        self.layout.addRow("States:", self.node_states)
        self.layout.addRow("Bounds:", self.node_bounds)
        self.layout.addRow("Object Depth:", self.node_object_depth)
        self.layout.addRow("Index in parent:", self.node_index_in_parent)
        # self.layout.addRow("Parent:", self.node_parent)
        # self.layout.addRow("Children:", self.node_children)
        self.layout.addRow("Children count:", self.node_children_count)
        self.layout.addRow(
            "Supports AccessibleComponent:", self.node_supports_acc_component
        )
        self.layout.addRow("Supports AccessibleAction:", self.node_supports_acc_action)
        self.layout.addRow(
            "Supports AccessibleSelection:", self.node_supports_acc_selection
        )
        self.layout.addRow("Supports AccessibleText:", self.node_supports_acc_text)

    def display_node(self, node: AccessibleNode | None):
        if node is None:
            self.node_name.setText("")
            self.node_description.setText("")
            self.node_role.setText("")
            self.node_states.setText("")
            self.node_bounds.setText("")
            self.node_object_depth.setText("")
            self.node_index_in_parent.setText("")
            self.node_children_count.setText("")
            self.node_supports_acc_component.setText("")
            self.node_supports_acc_action.setText("")
            self.node_supports_acc_selection.setText("")
            self.node_supports_acc_text.setText("")
            return

        self.node_role.setText(node.role)
        self.node_name.setText(node.name or "-")
        self.node_description.setText(node.description or "-")

        self.node_states.setText(",".join(node.states))

        bounds_text = f"x={node.bounds.x}; y={node.bounds.y}; width={node.bounds.width}; height={node.bounds.height}"
        self.node_bounds.setText(bounds_text)

        self.node_object_depth.setText(str(node.object_depth))
        self.node_index_in_parent.setText(str(node.index_in_parent))
        self.node_children_count.setText(str(len(node.children)))

        # self.node_parent.setText(node.parent)
        # self.node_children.setText(node.children)

        self.node_supports_acc_component.setText(str(node.supports_acc_component))
        self.node_supports_acc_action.setText(str(node.supports_acc_action))
        self.node_supports_acc_selection.setText(str(node.supports_acc_selection))
        self.node_supports_acc_text.setText(str(node.supports_acc_text))
