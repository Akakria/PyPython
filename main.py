#Author:        Artturi Kakriainen
#File:          main.py
#Description:   Driver code for the program

from keyboard import get_hotkey_name, send
from time import perf_counter
from os import system
from random import choice

import cursorManager
from board import Board
from player import Snake
from userInterface import UserInterface
from boardObjects import BoardObject


class Main:

    def __init__(self, board, snake, boardObject, interface, scoreFile, scale = 10):

        self.scoreFile = scoreFile
        self.ui = interface
        self.boardScale = scale
        self.board = board
        self.snake = snake
        self.trunk = self.snake.trunk
        self.object = boardObject
        self.score = 0
        self.highScore = self.getHighScore()
        self.updateRate = 0.4
        self.key = list(self.snake.keys.keys())[0]


    def newGame(self):

        self.board.board = self.board.genBoard(self.boardScale)
        self.snake.headPos = self.snake.initHeadPos.copy()
        self.snake.trunk = self.snake.initTrunk(3, self.snake.headPos)
        self.key = "w"
        self.snake.heading = "w"
        self.score = 0
        self.ui.splashPrint(system)
        cursorManager.setCursorPosition(6,0,"")
        

    def getHighScore(self):

        try:
            with open(self.scoreFile, "r+") as file:
                saved = int(file.read())

                if saved > self.score:
                    return saved
                else:
                    file.seek(0)
                    file.write(str(self.score))
                    file.truncate()
                    return self.score
            
        except:
            with open(self.scoreFile, "w+") as file:
                file.write("0")
                return 0
        
       
    def main(self):

        self.ui.splashPrint(system)  
        
        timer = perf_counter()
        
        while True:
            
            
            cycleUpdate = perf_counter()
            
            if get_hotkey_name() in self.snake.keys.keys():
                self.key = self.snake.keyEvent(get_hotkey_name)

            if cycleUpdate >= timer + self.updateRate:
                self.snake.moveHead(self.key)
                self.snake.incrementTrunk()
                
                
                if self.snake.checkCollision(self.boardScale) == True:
                    self.highScore = self.getHighScore()
                    self.ui.loseScreen(self.score, self.highScore, system, send)
                    self.newGame()
                    
                self.object.checkFood(self.snake.headPos)
          
                if self.object.check == True:
                    self.object.removeFood(self.snake.headPos)
                    self.score += 1
                    self.snake.growTrunk()
                    
                elif self.object.check == False and self.object.foodSpawned == False:
                    self.object.spawnFood(self.board, self.snake, choice)
        
                self.board.updatePositions(self.snake, self.object)

                self.ui.printBoard(self.board.board, self.boardScale, self.score, self.highScore)   
                timer = perf_counter()
                
            cursorManager.setCursorPosition(6,0,"")

       
if __name__ == '__main__':
    
    lines = 25
    col = 45
    
    system("mode con cols={0} lines={1}".format(str(col),str(lines)))
    cursorManager.hideCursor()
    boardScale = 14
    initHeadPos = [int(boardScale/2),int(boardScale/2)]
    
    main = Main(Board(boardScale), Snake(initHeadPos), BoardObject(), UserInterface(), "highscore.txt", boardScale)
    main.main()

    
