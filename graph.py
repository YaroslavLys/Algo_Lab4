from collections import defaultdict
from color import Color
from action import Action


class Graph:
    @staticmethod
    def build_graph(edges):
        graph = defaultdict(list)
        for x, y in edges:
            graph[x].append(y)
        return graph

    @staticmethod
    def dfs_iter(graph, start):
        cycle_is_present = False
        state = {v: Color.WHITE for v in graph}
        stack = [(Action.ENTER, start)]
        while stack:
            action, v = stack.pop()
            if action == Action.EXIT:
                state[v] = Color.BLACK
            else:
                state[v] = Color.GRAY
                stack.append((Action.EXIT, v))
                for n in graph[v]:
                    try:
                        if state[n] == Color.GRAY:
                            print('Found cycle at', n)
                            cycle_is_present = True
                        elif state[n] == Color.WHITE:
                            stack.append((Action.ENTER, n))
                    except KeyError:
                        pass
        return cycle_is_present
