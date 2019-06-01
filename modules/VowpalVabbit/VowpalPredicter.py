import subprocess
from modules.MapObjects.Tool import Tool
from modules.MapObjects.Saper import Saper
from modules.VowpalVabbit.CellState import CellState
from modules.VowpalVabbit.DataCreator import DataCreator
from modules.Board.Direction import Direction


class VowpalPredicter:

    def __init__(self, board):
        self.board = board

    def predict(self):
        point = self.board.getCordsOf(self.board.player)
        dataCreator = DataCreator()
        state = CellState()
        for yindex in range(-3, 4):
            for xindex in range(-3, 4):
                if(self.__doesVertexExist(point.x + xindex, point.y + yindex)):

                    if(self.board.board[point.y + yindex][point.x + xindex] is Tool):
                        state.cells[yindex + 3][xindex + 3] = 2
                    else:
                        state.cells[yindex + 3][xindex + 3] = 1

        dataCreator.addData(state)

        dataCreator.save("currentState")

        prediction = subprocess.check_output(
            "vw -i ./models/walking.model -t ./currentState -p /dev/stdout --quiet", shell=True)
        prediction = str(prediction)
        prediction = prediction.replace("b'", "")
        prediction = prediction.replace("\\", "")
        prediction = prediction.replace("n'", "")
        prediction = round(float(prediction))
        print(prediction)

        subprocess.os.remove("currentState")

        if(prediction == 0):
            return Direction.LEFT
        if(prediction == 1):
            return Direction.UP
        if(prediction == 2):
            return Direction.RIGHT
        if(prediction == 3):
            return Direction.DOWN

    def __doesVertexExist(self, x, y):
        if(x < 0 or x > 11 or y < 0 or y > 7):
            return False
        elif(self.board.board[y][x] is Tool or self.board.board[y][x] == None or self.board.board[y][x] is Saper):
            return True
        return False
