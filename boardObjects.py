#Author:        Artturi Kakriainen
#File:          boardObjects.py
#Description:   spawn/despawn scorables


class BoardObject:
    
    def __init__(self):
        
        self.foodMark = "ó"
        self.foodSpawned = False
        self.check = False
        self.foodPos = [0,0]


    def spawnFood(self, board, snake, choice):
        
        while True:
            
            row = choice(range(len(board.board) - 1))
            col = choice(range(len(board.board) - 1))
            foodPos = [row,col]
            
            if foodPos not in snake.trunk and foodPos != snake.headPos:
                self.foodPos = [row,col]
                self.foodSpawned = True
                break


    def removeFood(self,headPos):
        
        self.foodSpawned = False


    def checkFood(self, headPos):
        
        if headPos == self.foodPos:
            self.check = True
        else:
            self.check = False
