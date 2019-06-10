from sklearn import tree
from joblib import dump


class TreeCreator:

    def __init__(self):
        self.datas = []

    def addData(self, state):
        self.datas.append(state)

    def save(self, name):
        clf = tree.DecisionTreeClassifier()
        argumentsList = []
        resultsList = []
        for data in self.datas:
            resultsList.append(data.result)
            argumentsList.append(data.getCellsInArray())

        clf = clf.fit(argumentsList, resultsList)
        dump(clf, name)
