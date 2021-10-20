import unittest
from graph import Graph


class TestGraph(unittest.TestCase):

    def test1_dfs_iter(self):
        graph = Graph.build_graph([(0, 1), (1, 2), (0, 2), (3, 6), (6, 0)])
        self.assertEqual(Graph.dfs_iter(graph, 0), False)

    def test2_dfs_iter(self):
        graph = Graph.build_graph([(0, 1), (1, 2), (2, 3), (3, 0)])
        self.assertEqual(Graph.dfs_iter(graph, 0), True)
