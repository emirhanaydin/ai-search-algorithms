from __future__ import annotations

from dataclasses import dataclass
from itertools import chain
from typing import TypeVar, Generic, Optional

from edge import Edge
from vertex import Vertex

T = TypeVar("T")


@dataclass(frozen=True)
class Node(Generic[T]):
    __slots__ = ["vertex", "edge", "to"]

    vertex: Vertex[T]
    edge: Edge
    to: Optional[Vertex[T]]

    def __hash__(self):
        return hash((self.vertex, self.edge, self.to))

    def __lt__(self, other):
        return isinstance(other, Node) and self.edge < other.edge

    def __str__(self):
        return f"{self.vertex} -> {self.to} ({self.edge})"

    def __unicode__(self):
        return self.__str__

    def __repr__(self):
        return self.__str__


class GraphBuilderVertex(Generic[T]):
    __nodes__: tuple[Node[T]]
    __vertex__: Vertex[T]

    def __init__(self, vertex: Vertex[T]):
        self.__nodes__ = tuple[Node[T]]()
        self.__vertex__ = vertex

    def get_vertex(self):
        return self.__vertex__

    def get_nodes(self):
        return self.__nodes__

    def edge(self, to: T, cost: int):
        if to is not None:
            to = Vertex(to)
        vertex = self.__vertex__
        self.__nodes__ = tuple(list(chain.from_iterable([self.__nodes__, [Node[T](vertex, Edge(cost), to)]])))
        return self


class GraphBuilder(Generic[T]):
    __vertices__: tuple[GraphBuilderVertex[T]]

    def __init__(self):
        self.__vertices__ = tuple[GraphBuilderVertex[T]]()

    def vertex(self, value: T):
        builder_vertex = GraphBuilderVertex(Vertex(value))
        self.__vertices__ = tuple(list(chain.from_iterable([self.__vertices__, [builder_vertex]])))
        return builder_vertex

    def build(self):
        node_lists = [v.get_nodes() for v in self.__vertices__]
        nodes = tuple(list(chain.from_iterable(node_lists)))
        return Graph(nodes)


@dataclass(frozen=True)
class Graph(Generic[T]):
    __slots__ = ["nodes"]

    nodes: tuple[Node[T]]
