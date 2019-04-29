from modules.PathFinder.dfs.GraphCreator import GraphCreator
from modules.PathFinder.dfs.Graph import Graph


class PathFinder:

    @staticmethod
    def getPathToByDfs(board, x, y):
        graphCreator = GraphCreator(board)
        graph = graphCreator.createGraph()
        graph.dfs()
        steps = graph.getPathTo(graphCreator.getVertexByCords(x, y))
        return steps
