from PySide6.QtWidgets import QTreeWidget, QTreeWidgetItem

from ..core.backend import AccessibleNode
from ..core.controller import Controller


class TreeItem(QTreeWidgetItem):
    def __init__(self, node: AccessibleNode):
        super().__init__([
            # node.name or "-",
            node.role
        ])
        self.node = node


class TreePanel(QTreeWidget):
    def __init__(self, controller: Controller):
        super().__init__()

        self.controller = controller

        # self.setHeaderLabels(["Name", "Role"])
        self.populate()

        self.itemClicked.connect(self.on_click)

    def populate(self):
        for root in self.controller.roots():
            item = self.build_item(root)
            self.addTopLevelItem(item)

    def build_item(self, node: AccessibleNode) -> TreeItem:
        item = TreeItem(node)

        for child in node.children:
            item.addChild(self.build_item(child))

        return item

    def on_click(self, item: TreeItem):
        node = item.node
        self.controller.select_node(node)
