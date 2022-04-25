from typing import TypeVar, Generic

from graph_searcher import GraphSearcher
from vertex import Vertex

T = TypeVar("T")


class BFS(GraphSearcher, Generic[T]):
    def __search__(self, node: Vertex[T]) -> tuple[bool, int]:
        queue = self.__buffer__
        current = queue.pop(0)
        visited = self.__visited__
        vertices = self.__vertices__[current]

        for vertex in vertices:
            if vertex == node:
                visited[vertex] = True
                return True, 0
            if vertex not in visited:
                visited[vertex] = True
                queue.append(vertex)

        return False, 0
