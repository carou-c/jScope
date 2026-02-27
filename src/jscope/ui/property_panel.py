from PySide6.QtWidgets import QWidget, QTreeWidget, QTreeWidgetItem, QAbstractItemView

from ..core.models import AccessibleNode


class PropertyPanel(QTreeWidget):
    def __init__(self, parent: QWidget | None):
        super().__init__(parent=parent)
        self.setHeaderLabels(["Property", "Value"])

        self.setSelectionMode(QAbstractItemView.SelectionMode.ExtendedSelection)
        self.setAllColumnsShowFocus(True)

        self.node_name = QTreeWidgetItem(self, ["name", ""])
        self.node_description = QTreeWidgetItem(self, ["description", ""])
        self.node_role = QTreeWidgetItem(self, ["role", ""])
        self.node_states = QTreeWidgetItem(self, ["states", ""])

        self.node_bounds = QTreeWidgetItem(self, ["bounds", ""])
        self.node_bounds_x = QTreeWidgetItem(self.node_bounds, ["x", ""])
        self.node_bounds_y = QTreeWidgetItem(self.node_bounds, ["y", ""])
        self.node_bounds_width = QTreeWidgetItem(self.node_bounds, ["width", ""])
        self.node_bounds_height = QTreeWidgetItem(self.node_bounds, ["height", ""])
        self.node_bounds.addChildren(
            [
                self.node_bounds_x,
                self.node_bounds_y,
                self.node_bounds_width,
                self.node_bounds_height,
            ]
        )

        self.node_object_depth = QTreeWidgetItem(self, ["object_depth", ""])
        self.node_index_in_parent = QTreeWidgetItem(self, ["index_in_parent", ""])
        # self.node_parent = QTreeWidgetItem(self)
        self.node_children_count = QTreeWidgetItem(self, ["children_count", ""])
        self.node_supports_acc_component = QTreeWidgetItem(
            self, ["supports_accessible_text", ""]
        )
        self.node_supports_acc_action = QTreeWidgetItem(
            self, ["supports_accessible_action", ""]
        )
        self.node_supports_acc_selection = QTreeWidgetItem(
            self, ["supports_accessible_selection", ""]
        )
        self.node_supports_acc_text = QTreeWidgetItem(
            self, ["supports_accessible_text", ""]
        )

    def display_node(self, node: AccessibleNode | None):
        self.node_name.setText(1, "")
        self.node_description.setText(1, "")
        self.node_role.setText(1, "")

        for child in self.node_states.takeChildren():
            self.node_states.removeChild(child)

        self.node_bounds_x.setText(1, "")
        self.node_bounds_y.setText(1, "")
        self.node_bounds_width.setText(1, "")
        self.node_bounds_height.setText(1, "")

        self.node_object_depth.setText(1, "")
        self.node_index_in_parent.setText(1, "")
        self.node_children_count.setText(1, "")

        self.node_supports_acc_component.setText(1, "")
        self.node_supports_acc_action.setText(1, "")
        self.node_supports_acc_selection.setText(1, "")
        self.node_supports_acc_text.setText(1, "")

        if node is None:
            return

        self.node_role.setText(1, node.role)
        self.node_name.setText(1, node.name or "-")
        self.node_description.setText(1, node.description or "-")

        for state in node.states:
            self.node_states.addChild(QTreeWidgetItem(["", state]))

        self.node_bounds_x.setText(1, str(node.bounds.x))
        self.node_bounds_y.setText(1, str(node.bounds.y))
        self.node_bounds_width.setText(1, str(node.bounds.width))
        self.node_bounds_height.setText(1, str(node.bounds.height))

        self.node_object_depth.setText(1, str(node.object_depth))
        self.node_index_in_parent.setText(1, str(node.index_in_parent))
        self.node_children_count.setText(1, str(len(node.children)))

        self.node_supports_acc_component.setText(1, str(node.supports_acc_component))
        self.node_supports_acc_action.setText(1, str(node.supports_acc_action))
        self.node_supports_acc_selection.setText(1, str(node.supports_acc_selection))
        self.node_supports_acc_text.setText(1, str(node.supports_acc_text))
