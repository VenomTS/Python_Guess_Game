class Spot:
    def __init__(self, x, y, letter):
        self.row = x
        self.col = y
        self.letter = letter

class Board:
    def __init__(self, sentence):
        self.sentence = sentence
        self.modifySentence()
        self.n = len(self.sentence)
        self.board = []
        self.selected = []
        self.hidden = []
        self.createBoard()

    def modifySentence(self):
        text = ""
        for item in self.sentence:
            if item != " ":
                text += item
        self.sentence = text.upper()

    def createBoard(self):
        currLetter = 0
        for row in range(self.n):
            self.board.append([])
            for i in range(self.n):
                self.board[row].append(Spot(row, i, self.sentence[currLetter]))
            currLetter += 1

    def selectSpot(self, x, y):
        spot = self.board[x][y]
        if self.checkValid(x, y):
            self.selected.append(spot)
            for i in range(self.n):
                if self.board[x][i] != spot:
                    self.hidden.append(self.board[x][i])
                if self.board[i][y] != spot:
                    self.hidden.append(self.board[i][y])

    def checkValid(self, x, y):
        spot = self.board[x][y]
        if spot in self.hidden or spot in self.selected:
            return False
        return True