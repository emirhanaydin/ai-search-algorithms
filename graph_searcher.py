from abc import ABC, abstractmethod
from typing import TypeVar, Generic

from graph import Graph
from vertex import Vertex

T = TypeVar("T")


class GraphSearcher(ABC, Generic[T]):
    __slots__ = ["graph"]
    __visited__: dict[Vertex[T], int]
    __buffer__: list[Vertex[T]]

    __vertices__: dict[Vertex[T], dict[Vertex[T], int]]

    graph: Graph

    def __init__(self, graph: Graph):
        self.graph = graph

        vertices = {}
        for node in graph.nodes:
            vertex = node.vertex
            connections = vertices[vertex] if vertex in vertices else {}
            connections[node.to] = node.edge.cost
            vertices[vertex] = connections
        self.__vertices__ = vertices

    @abstractmethod
    def __search__(self, vertex: Vertex) -> tuple[bool, int]:
        pass

    def __visited_to_generic__(self) -> list[T]:
        return [vertex.value for vertex in self.__visited__]

    def search(self, value: T, start: T = None) -> tuple[list[Vertex], int]:
        vertices = self.__vertices__
        if start is None:
            start = list(vertices.keys())[0].value

        value = Vertex[T](value)
        start = Vertex[T](start)

        initial_result = [start]
        if start == value:
            return initial_result, 0

        self.__visited__ = {start: 0}
        buffer = self.__buffer__ = initial_result.copy()

        while len(buffer) > 0:
            found, cost = self.__search__(value)
            if found:
                return self.__visited_to_generic__(), cost

        return self.__visited_to_generic__(), 0
