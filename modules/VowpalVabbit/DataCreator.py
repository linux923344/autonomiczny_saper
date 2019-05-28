
class DataCreator:

    def __init__(self):
        self.datas = []

    def addData(self, leftCell, upCell, rightCell, downCell):
        resultString = "LeftCell:" + str(leftCell) + " UpCell:" + str(
            upCell) + " RightCell:" + str(rightCell) + " DownCell:" + str(downCell)
        self.datas.append(resultString)

    def save(self, name):
        f = open(name, "w")
        for line in self.datas:
            f.write(line + "\n")
        f.close()
