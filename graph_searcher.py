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
    __vertex_backtrace__: dict[Vertex[T], dict[Vertex[T]]]

    graph: Graph

    def __init__(self, graph: Graph):
        self.graph = graph

        vertices = {}
        vertex_backtrace = {}
        for node in graph.nodes:
            vertex = node.vertex
            connections = vertices[vertex] if vertex in vertices else {}
            connections[node.to] = node.edge.cost
            vertices[vertex] = connections
            backtrace = vertex_backtrace[node.to] if node.to in vertex_backtrace else {}
            backtrace[vertex] = True
            vertex_backtrace[node.to] = backtrace
        self.__vertices__ = vertices
        self.__vertex_backtrace__ = vertex_backtrace

    @abstractmethod
    def __search__(self, vertex: Vertex) -> tuple[bool, int]:
        pass

    def __visited_to_generic__(self) -> list[T]:
        return [vertex.value for vertex in self.__visited__]

    def search(self, value: T, start: T = None) -> tuple[list[Vertex[T]], int]:
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

    def get_path(self) -> list[Vertex[T]]:
        visited = list(self.__visited__.keys())
        backtrace = self.__vertex_backtrace__
        step_vertex = visited.pop()
        path = [step_vertex.value]
        for vertex in visited[::-1]:
            if step_vertex in backtrace[vertex]:
                path.append(vertex.value)
                step_vertex = vertex

        path.reverse()
        return path
