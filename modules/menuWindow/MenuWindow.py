from tkinter import *
from os import listdir
import os
from os.path import isfile, join
from modules.menuWindow.AlgorythmType import AlgorythmType
from modules.Board.GameStarter import GameStarter


class MenuWindow(Tk):

    def __init__(self):
        super(MenuWindow, self).__init__()
        self.resizable(False, False)
        self.title("Autonomiczny Saper")
        maplabel = Label(self, text="Wybór mapy")
        maplabel.grid(column=0, row=0)
        algorytmLabel = Label(self, text="Wybór algorytmu: ")
        algorytmLabel.grid(column=0, row=3)
        self.variable = Variable(self)
        self.variable.set(AlgorythmType.BEST_FIRST_SEARCH)  # default value

        self.algorytmSelector = OptionMenu(self, self.variable, AlgorythmType.BEST_FIRST_SEARCH, AlgorythmType.BREADTH_FIRST_SEARCH,
                                           AlgorythmType.DFS, AlgorythmType.VOWPAL_WABBIT, AlgorythmType.DECISION_TREE)

        self.variable.trace("w", self.get_selection)

        self.algorytmSelector.grid(column=0, row=4)

        self.maplist = Listbox(self)
        self.maplist.config(width=100)

        for index, mapElement in enumerate(self.__getMapList()):
            self.maplist.insert(index+1, mapElement)

        self.maplist.grid(column=0, row=1)

        btn = Button(self, text="START", command=self.start)

        btn.grid(column=0, row=5)

    def get_selection(self):
        print("Selected: " + self.variable.get())

    def __getMapList(self):
        allFiles = [f for f in listdir(
            "./maps/") if isfile(join("./maps/", f))]
        return allFiles

    def start(self):
        GameStarter.run(self.maplist.get(ACTIVE), self.variable.get())
        # self.quit()
