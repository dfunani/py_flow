from typing import Tuple
from pydantic import BaseModel, ConfigDict
from console.canvas import Canvas, NodeTypes
from models.nodes import INode
from models.types import Primitive


class PrimitiveNode(INode, BaseModel):
    node: Primitive
    model_config = ConfigDict(extra="allow")

    def __init__(self, node: Primitive, canvas: Canvas) -> None:
        super(PrimitiveNode, self).__init__(node=node)
        self.canvas = canvas

    def draw(self, position: Tuple[int, int]):
        self.canvas.add_node(
            position,
            NodeTypes.PRIMITIVE,
            {"value": self.node, "type": type(self.node).__name__},
        )
