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
