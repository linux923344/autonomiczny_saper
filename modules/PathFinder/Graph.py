from modules.PathFinder.Vertex import Vertex


class Graph:
    def __init__(self, successorsList):
        self.successorsList = successorsList

    def dfs(self):
        for v in self.successorsList:
            if(v.visited == False):
                self.visiteVertex(v, None)

    def visiteVertex(self, v, parent):
        v.visited = True
        v.parent = parent
        for successor in self.successorsList[v]:
            if(successor.visited == False):
                self.visiteVertex(successor, v)

    def getPathTo(self, v):
        pass
