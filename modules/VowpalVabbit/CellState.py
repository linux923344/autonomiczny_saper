class CellState:

    def __init__(self):
        self.cells = [[0 for i in range(7)] for i in range(7)]
        self.result = 0

    def getCellsInArray(self):
        result = []
        for y_line in self.cells:
            for cell in y_line:
                result.append(cell)

        return result
