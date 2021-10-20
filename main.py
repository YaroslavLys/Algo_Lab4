from graph import Graph


if __name__ == '__main__':
    input_file = "in.txt"
    with open(input_file, mode="r") as f:
        n = int(f.readline())
        EDGES = []
        for i in range(n):
            edge = list(map(int, f.readline().split(" ")))
            EDGES.append(edge)
    graph = Graph.build_graph(EDGES)
    Graph.dfs_iter(graph, 0)
