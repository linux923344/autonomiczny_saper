from modules.PathFinder.BestFirstSearch.Vertex import Vertex
from modules.Board.Direction import Direction
from modules.Board.DirectionCalculator import DirectionCalculator
from modules.VowpalVabbit.DataCreator import DataCreator
from modules.VowpalVabbit.CellState import CellState
from queue import PriorityQueue
import math


class GraphBestFS:
    def __init__(self, successorsList):
        self.successorsList = successorsList
        self.q = PriorityQueue()
        self.currentVertex = None
        self.learningData = DataCreator()

    def setDestinations(self, destinations):
        self.destinations = destinations

    def setPriorities(self):
        for v in self.successorsList:
            for successor in self.successorsList[v]:
                direction = DirectionCalculator.getDirectionByChords(
                    v.x, v.y, successor.x, successor.y)
                distance = self.getNearestDestination(v, direction)
                successor.priority = distance

    def getNearestDestination(self, v, direction):
        distance = math.inf
        for destination in self.destinations:
            if(direction == Direction.UP):
                if(destination.y > v.y):
                    current_distance = abs(
                        destination.x-v.x) + abs(destination.y - v.y)
                    distance = min(distance, current_distance)
            elif(direction == Direction.DOWN):
                if(destination.y < v.y):
                    current_distance = abs(
                        destination.x-v.x) + abs(destination.y - v.y)
                    distance = min(distance, current_distance)
            elif(direction == Direction.LEFT):
                if(destination.x < v.x):
                    current_distance = abs(
                        destination.x-v.x) + abs(destination.y - v.y)
                    distance = min(distance, current_distance)
            elif(direction == Direction.RIGHT):
                if(destination.x > v.x):
                    current_distance = abs(
                        destination.x-v.x) + abs(destination.y - v.y)
                    distance = min(distance, current_distance)
        return distance

    def __bestFirstSearch(self, startv):
        self.q.put(startv)
        startv.visited = True
        while not self.q.empty():
            v = self.q.get()

            for successor in self.successorsList.get(v):
                if successor.visited == False:
                    self.q.put(successor)
                    successor.visited = True
                    successor.parent = v

    def bestFirstSearch(self):
        startv = list(self.successorsList.keys())[0]
        self.__bestFirstSearch(startv)

    def getPathTo(self, v):
        vpoint = v
        path = []
        states = []

        while(vpoint.parent != None):

            state = CellState()

            if(vpoint.x < vpoint.parent.x):
                path.append(Direction.LEFT)
                state.result = 0

            elif(vpoint.x > vpoint.parent.x):
                path.append(Direction.RIGHT)
                state.result = 2

            elif(vpoint.y > vpoint.parent.y):

                path.append(Direction.DOWN)
                state.result = 3
            else:

                path.append(Direction.UP)
                state.result = 1

            for successor in self.successorsList[vpoint.parent]:
                direction = DirectionCalculator.getDirectionByChords(
                    vpoint.parent.x, vpoint.parent.y, successor.x, successor.y)

                if(direction == Direction.DOWN):
                    state.downCell = 1
                if(direction == Direction.UP):
                    state.upCell = 1
                if(direction == Direction.LEFT):
                    state.leftCell = 1
                if(direction == Direction.RIGHT):
                    state.rightCell = 1

            states.append(state)

            vpoint = vpoint.parent

        states.reverse()
        for state in states:
            self.learningData.addData(state)

        path.reverse()
        return path

    def resetSearch(self):
        for v in self.successorsList:
            v.visited = False
            v.parent = None
            v.priority = None
        self.setPriorities()

    def getVertexByCords(self, x, y):
        for v in self.successorsList:
            if(v.x == x and v.y == y):
                return v

    def getWholePath(self):
        finalPath = []
        startv = list(self.successorsList.keys())[0]
        self.currentVertex = startv
        for destination in self.destinations:
            self.resetSearch()
            self.__bestFirstSearch(self.currentVertex)
            goalVertex = self.getVertexByCords(destination.x, destination.y)
            finalPath += self.getPathTo(goalVertex)
            self.currentVertex = goalVertex

        return finalPath

    def savePathToFile(self, name):
        self.learningData.save(name)
