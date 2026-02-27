from pyjab.common.exceptions import JABException

from pyjab.jabelement import JABElement
from pyjab.jabdriver import JABDriver

from ..core.models import AccessibleRole, AccessibleState, AccessibleNode, Bounds


class PyjabBackend:
    def __init__(self, driver: JABDriver) -> None:
        self.driver: JABDriver = driver
        self.__nodes: list[AccessibleNode] = []
        self.refresh()

    def _build_node_tree(
        self,
        element: JABElement,
        parent_id: int | None,
    ):
        id = len(self.__nodes)
        self.__nodes.append(None)  # type: ignore
        children: list[JABElement]
        depth = element.object_depth
        try:
            children = element.find_elements_by_object_depth(depth + 1, False)
        except JABException:
            children = []

        node = AccessibleNode(
            id=id,
            name=element.name,
            description=element.description,
            role=AccessibleRole(element.role.lower().replace(" ", "_")),
            states={
                AccessibleState(state.lower().replace(" ", "_"))
                for state in element.states.split(",")
            },
            bounds=Bounds(
                x=element.bounds["x"],
                y=element.bounds["y"],
                width=element.bounds["width"],
                height=element.bounds["height"],
            ),
            object_depth=depth,
            index_in_parent=element.index_in_parent,
            parent_id=parent_id,
            children=[self._build_node_tree(child, id) for child in children],
            supports_acc_component=element.accessible_component,
            supports_acc_action=element.accessible_action,
            supports_acc_selection=element.accessible_selection,
            supports_acc_text=element.accessible_text,
            text=element.text if element.accessible_text else None,
        )

        self.__nodes[id] = node

    def refresh(self) -> None:
        self.__nodes.clear()
        root = self.driver.root_element

        self._build_node_tree(root, None)

    def highlight(self, node: AccessibleNode):
        print("Placeholder Highlight:", node)

    def get_root_nodes(self) -> list[AccessibleNode]:
        return self.__nodes[:1]
