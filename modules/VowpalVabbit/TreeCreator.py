from sklearn import tree
from joblib import dump, load
from sklearn.tree import export_graphviz
from sklearn.externals.six import StringIO
from IPython.display import Image
import pydotplus


class TreeCreator:

    def __init__(self):
        self.datas = []

    def addData(self, state):
        self.datas.append(state)

    def save(self, name):
        clf = load("./models/walkingdecision.model.joblib")
        feature_cols = ["x", "x", "x", "x", "x", "x", "x", "x", "x", "x", "x", "x", "x", "x", "x", "x", "x", "x", "x", "x", "x", "x", "x",
                        "x", "x", "x", "x", "x", "x", "x", "x", "x", "x", "x", "x", "x", "x", "x", "x", "x", "x", "x", "x", "x", "x", "x", "x", "x", "x"]
        argumentsList = []
        resultsList = []
        for data in self.datas:
            resultsList.append(data.result)
            argumentsList.append(data.getCellsInArray())

        clf = clf.fit(argumentsList, resultsList)

        dot_data = StringIO()
        export_graphviz(clf, out_file=dot_data,
                        filled=True, rounded=True,
                        special_characters=True, feature_names=feature_cols, class_names=feature_cols)
        graph = pydotplus.graph_from_dot_data(dot_data.getvalue())
        graph.write_png('diabetes.png')
        Image(graph.create_png())

        dump(clf, name)
