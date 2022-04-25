from typing import TypeVar, Generic

from graph import Graph
from graph_searcher import GraphSearcher
from vertex import Vertex

T = TypeVar("T")


class UCS(GraphSearcher, Generic[T]):
    __queue__: list[tuple[Vertex[T], int]]
    __was_queue_init__: bool

    def __init__(self, graph: Graph):
        super().__init__(graph)
        self.__queue__ = []
        self.__was_queue_init__ = False

    def __search__(self, node: Vertex[T]) -> tuple[bool, int]:
        visited = self.__visited__
        queue = self.__queue__
        if len(visited) < 2 and not self.__was_queue_init__:
            k, v = list(visited.items())[0]
            self.__queue__ = [(k, v)]
            queue = self.__queue__
            self.__was_queue_init__ = True
        else:
            self.__was_queue_init__ = False

        current, current_cost = queue.pop(0)
        vertices = self.__vertices__[current]

        if current not in visited:
            visited[current] = current_cost

        # if current == node:
        #     return True, current_cost

        for vertex, cost in vertices.items():
            c = current_cost + cost

            if vertex == node:
                self.__visited__[vertex] = c
                return True, c

            if vertex not in visited:
                queue.append((vertex, c))
                queue = self.__queue__ = sorted(queue, key=lambda x: x[1])
                self.__buffer__ = queue

        return False, current_cost
