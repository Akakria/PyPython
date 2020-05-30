#Author:        Artturi Kakriainen
#File:          board.py
#Description:   x by x game board for console game


class Board:

    def __init__(self, scale):

        self.scale = scale
        self.boardCell = " "
        self.board = self.genBoard(self.scale)
        
        
    def genBoard(self,scale):

        board = []
        rowTemplate = scale * [self.boardCell]

        for i in range(scale):
            board.append(rowTemplate.copy())

        return board

            
    def updatePositions(self, snake, boardObject):

        if boardObject.foodSpawned == True:
            self.board[boardObject.foodPos[0]][boardObject.foodPos[1]] = boardObject.foodMark
        
        for i in snake.trunk:           
            self.board[i[0]][i[1]] = snake.bodyPart  

        self.board[snake.clearTail[0]][snake.clearTail[1]] = self.boardCell
        
        self.board[snake.headPos[0]][snake.headPos[1]] = snake.head[snake.heading]
