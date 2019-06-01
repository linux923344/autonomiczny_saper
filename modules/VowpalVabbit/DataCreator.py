from modules.VowpalVabbit.CellState import CellState


class DataCreator:

    def __init__(self):
        self.datas = []

    def addData(self, state):
        self.datas.append(state)

    def save(self, name):
        f = open(name, "w")
        for line in self.datas:
            f.write(str(line.result) + " | " + "LeftCell: " + str(line.leftCell) + " RightCell: " +
                    str(line.rightCell) + " UpCell: " + str(line.upCell) + " DownCell: " + str(line.downCell) + "\n")
        f.close()
