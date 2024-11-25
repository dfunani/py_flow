from pydantic import BaseModel
from models.nodes import INode
from models.types import Primitive


class PrimitiveNode(INode, BaseModel):
    node: Primitive

    def __init__(self, node: Primitive) -> None:
        super(PrimitiveNode, self).__init__(node=node)
        # self.node = node

    def draw(self, offset: int = 1):
        print(f"{offset * ' '}{self.node}")
