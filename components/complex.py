from collections.abc import Iterable
from typing import Any, Dict, List, ItemsView, Tuple
from pydantic import BaseModel, ConfigDict
from components.primitive import PrimitiveNode
from console.canvas import Canvas, NodeTypes
from models.nodes import INode
from models.types import Complex, Primitive


class ComplexNode(INode, BaseModel):
    nodes: Complex
    model_config = ConfigDict(extra="allow")

    def __init__(self, nodes: Complex, canvas: Canvas) -> None:
        super(ComplexNode, self).__init__(nodes=nodes)
        self.canvas = canvas

    def draw(self, position: Tuple[int, int]):
        nodes: (
            enumerate[Complex | Primitive] | Iterable[Tuple[str, Complex | Primitive]]
        ) = self.create_iterator()
        self.canvas.add_node(position, NodeTypes.COMPLEX, {"value": self.nodes, "type": type(self.nodes).__name__})
        offset_x = position[0] + 200
        for key, node in nodes:
            position = (offset_x, position[1])
            if isinstance(node, (List, Dict)):
                ComplexNode(node, self.canvas).draw(position)
            else:
                PrimitiveNode(node, self.canvas).draw(position)
                position = (offset_x, position[1] + 150)

    def create_iterator(
        self,
    ) -> enumerate[Complex | Primitive] | Iterable[Tuple[str, Complex | Primitive]]:
        if isinstance(self.nodes, List):
            return enumerate(self.nodes)
        else:
            return self.nodes.items()
