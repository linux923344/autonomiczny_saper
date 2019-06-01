from modules.VowpalVabbit.CellState import CellState
import inflect


class DataCreator:

    def __init__(self):
        self.datas = []

    def addData(self, state):
        self.datas.append(state)

    def save(self, name):
        f = open(name, "w")
        resultString = ""
        numberTranslator = inflect.engine()
        for line in self.datas:
            resultString += (str(line.result) + " |")
            for yindex, ycell in enumerate(line.cells):
                for xindex, xcell in enumerate(ycell):
                    resultString += (" " + numberTranslator.number_to_words(yindex) +
                                     numberTranslator.number_to_words(xindex)+":" + str(xcell))
            resultString += "\n"
        f.write(resultString)
        f.close()
