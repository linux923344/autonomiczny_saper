from modules.VowpalVabbit.DataCreator import DataCreator


class LearningData:

    def __init__(self):
        self.dataCreator = DataCreator()

    def addData(self, leftCell, upCell, rightCell, downCell, result):
        resultString = "LeftCell:" + str(leftCell) + " UpCell:" + str(
            upCell) + " RightCell:" + str(rightCell) + " DownCell:" + str(downCell)
        resultString = str(result)+" | " + resultString
        self.dataCreator.datas.append(resultString)

    def save(self, name):
        self.dataCreator.save(name)
