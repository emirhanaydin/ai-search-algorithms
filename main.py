from bfs import BFS
from dfs import DFS
from graph import GraphBuilder
from ucs import UCS


def main():
    builder = GraphBuilder()
    builder.vertex("A").edge("C", 3)
    builder.vertex("B").edge("I", 1)
    builder.vertex("C").edge("A", 3).edge("F", 5).edge("N", 5)
    builder.vertex("D").edge("F", 3).edge("H", 4).edge("J", 4)
    builder.vertex("E").edge("L", 1).edge("R", 3)
    builder.vertex("F").edge("C", 5).edge("D", 3).edge("G", 8).edge("R", 4)
    builder.vertex("G").edge("F", 8).edge("H", 7).edge("O", 4)
    builder.vertex("H").edge("D", 4).edge("G", 7).edge("J", 5).edge("K", 8)
    builder.vertex("I").edge("B", 1).edge("N", 4)
    builder.vertex("J").edge("D", 4).edge("H", 5).edge("K", 4)
    builder.vertex("K").edge("H", 8).edge("J", 4).edge("M", 4).edge("N", 7)
    builder.vertex("L").edge("E", 1)
    builder.vertex("M").edge("K", 4).edge("P", 4)
    builder.vertex("N").edge("C", 5).edge("I", 4).edge("K", 7)
    builder.vertex("O").edge("G", 4).edge("P", 4).edge("Q", 2)
    builder.vertex("P").edge("M", 4).edge("O", 4)
    builder.vertex("Q").edge("O", 2)
    builder.vertex("R").edge("E", 3).edge("F", 4)
    graph = builder.build()

    bfs = BFS(graph=graph)
    result, _ = bfs.search("Q", start="B")
    print(result)

    dfs = DFS(graph=graph)
    result, _ = dfs.search("Q", start="B")
    print(result)

    ucs = UCS(graph=graph)
    result, cost = ucs.search("Q", start="B")
    print(result, cost)


if __name__ == '__main__':
    main()
