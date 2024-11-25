from collections.abc import Iterable
from typing import Any, Dict, List, ItemsView, Tuple
from pydantic import BaseModel
from components.primitive import PrimitiveNode
from models.nodes import INode
from models.types import Complex, Primitive


class ComplexNode(INode, BaseModel):
    nodes: Complex

    def __init__(self, nodes: Complex) -> None:
        super(ComplexNode, self).__init__(nodes=nodes)

    def draw(self, offset: int = 1):
        nodes: (
            enumerate[Complex | Primitive] | Iterable[Tuple[str, Complex | Primitive]]
        ) = self.create_iterator()
        for key, node in nodes:
            print(f"{offset * ' '}Key: {key}")
            if isinstance(node, (List, Dict)):
                ComplexNode(node).draw(offset * 4)
            else:
                PrimitiveNode(node).draw(offset * 4)

    def create_iterator(
        self,
    ) -> enumerate[Complex | Primitive] | Iterable[Tuple[str, Complex | Primitive]]:
        if isinstance(self.nodes, List):
            return enumerate(self.nodes)
        else:
            return self.nodes.items()
