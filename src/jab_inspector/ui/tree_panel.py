from PySide6.QtWidgets import QTreeWidget, QTreeWidgetItem

from ..core.models import AccessibleNode
from ..core.controller import Controller


class TreeItem(QTreeWidgetItem):
    def __init__(self, node: AccessibleNode):
        super().__init__(
            [
                node.role,
                node.name or "-",
            ]
        )
        self.node: AccessibleNode = node


class TreePanel(QTreeWidget):
    def __init__(self, controller: Controller):
        super().__init__()

        self.controller = controller

        self.setHeaderLabels(["AccessibleRole", "Name"])
        self.setColumnWidth(0, 250)
        self.populate()

        self.itemClicked.connect(self.on_click)

    def populate(self):
        for root in self.controller.roots():
            item = self.build_item(root)
            self.addTopLevelItem(item)

    def rebuild(self):
        self.clear()
        self.populate()

    def build_item(self, node: AccessibleNode) -> TreeItem:
        item = TreeItem(node)

        for child in node.children:
            item.addChild(self.build_item(child))

        return item

    def on_click(self, item: TreeItem):
        node = item.node
        self.controller.select_node(node)
