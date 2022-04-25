from typing import TypeVar, Generic

from graph_searcher import GraphSearcher
from vertex import Vertex

T = TypeVar("T")


class DFS(GraphSearcher, Generic[T]):
    def __search__(self, node: Vertex[T]) -> tuple[bool, int]:
        stack = self.__buffer__
        current = stack.pop()
        visited = self.__visited__
        vertices = self.__vertices__[current]

        if current not in visited:
            visited[current] = True

        for vertex in vertices:
            if vertex == node:
                visited[vertex] = True
                return True, 0
            if vertex not in visited:
                stack.append(vertex)

        return False, 0
