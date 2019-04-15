from modules.PathFinder.Vertex import Vertex


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
