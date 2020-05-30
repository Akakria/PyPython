#Author:        Artturi Kakriainen
#File:          userInterface.py
#Description:   UI for console game

class UserInterface:
    
    def __init__(self):
        
        self.title = """      ___       ___       __  __          
     / _ \__ __/ _ \__ __/ /_/ / ___  ___ 
    / ___/ // / ___/ // / __/ _ / _ \/ _ \ 
   /_/   \_, /_/   \_, /\__/_//_\___/_//_/ 
        /___/     /___/  """

        self.gameOver = """

            _____                
           / ___/__ ___ _  ___    
          / (_ / _ `/  ' \/ -_)   
          \___/\_,_/_/_/_/\__/    
               ____               
              / __ \_  _____ ____ 
             / /_/ / |/ / -_) __/ 
             \____/|___/\__/_/
         """

    def splashPrint(self, system):
        system("cls")
        print(self.title)

        
    def printBoard(self, board, scale, score, highScore):
        
        print("     ",2 * scale * "█" + "█████")

        for i in board:
            print("      ██", *i , "██",sep = " ")

        print("     ",2 * scale * "█" + "█████")

        print("\n      SCORE:",score,"           HIGHSCORE:",highScore)

        
    def loseScreen(self, score, highScore, system, send):
        system("cls")
        
        send("ctrl + backspace")
        
        print(self.gameOver)
        
        
        print("\n\n\n         press <Enter> for new game")
        print("\n" * 6,"      SCORE:",score,"           HIGHSCORE:",highScore)
       
        input()
    

        
        
