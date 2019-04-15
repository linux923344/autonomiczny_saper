from modules.PathFinder.Vertex import Vertex
from modules.PathFinder.Graph import Graph


class PathFinder:

    def __init__(self, board):
        self.vertices = []
        self.board = board
        for indexline, line in enumerate(self.board.board):
            for indexrow, row in enumerate(line):
                if(row == None):
                    v = Vertex(indexrow, indexline)
                    self.vertices.append(v)

    def getVertexByCords(self, x, y):
        for v in self.vertices:
            if(v.x == x and v.y == y):
                return v
        return False

    def getSuccsessorsList(self, v):
        successors = []
        if v.y < 7 and self.board.board[v.y+1][v.x] == None:
            successor = self.getVertexByCords(v.x, v.y+1)
            successors.append(successor)
        if v.y > 0 and self.board.board[v.y-1][v.x] == None:
            successor = self.getVertexByCords(v.x, v.y-1)
            successors.append(successor)
        if v.x < 11 and self.board.board[v.y][v.x + 1] == None:
            successor = self.getVertexByCords(v.x + 1, v.y)
            successors.append(successor)
        if v.x > 0 and self.board.board[v.y][v.x - 1] == None:
            successor = self.getVertexByCords(v.x - 1, v.y)
            successors.append(successor)
        return successors

    def getAllSuccessorsList(self):
        dictionary = {}
        for v in self.vertices:
            successors = self.getSuccsessorsList(v)
            dictionary[v] = successors
        return dictionary

    def getPathTo(self, x, y):
        successorsList = self.getAllSuccessorsList()
        graph = Graph(successorsList)
        graph.dfs()
        graph.getPathTo(self.getVertexByCords(x, y))
