#Author:        Artturi Kakriainen
#File:          player.py
#Description:   Init and update snake

class Snake:

    def __init__(self, initHeadPos = [0,0]):

        self.head = {"w":"▲", "s":"▼", "a":"◄", "d":"►"}
        self.keys = {"w":"s","s":"w","a":"d","d":"a"}
        self.coordinate = {"w":(0,-1), "s":(0,1), "a":(1,-1), "d":(1,1)}
        self.heading = "w"
        self.bodyPart = "■"
        self.inverseDirection = self.keys[self.heading]
        self.initHeadPos = initHeadPos
        self.headPos = self.initHeadPos.copy()
        self.tempPos = [0,0]
        self.trunk = self.initTrunk(3, self.headPos)
        self.clearTail = [0,0]
           
    
    def initTrunk(self, length, headPos):
     
        trunk = [headPos.copy() for x in range(length)]
        tailRow = 1
        
        for i in trunk:
            i[0] += tailRow
            tailRow += 1

        return trunk


    def incrementTrunk(self):

        newPos = self.tempPos
        currentPos = [0,0]
        newTrunk = len(self.trunk) * [""]
        self.clearTail = self.trunk[-1]
        
        for index, i in enumerate(self.trunk):   
            currentPos = i
            i = newPos
            newPos = currentPos
            newTrunk[index] = i

        self.trunk = newTrunk

    
    def growTrunk(self):

        self.trunk.append(self.trunk[-1])


    def moveHead(self, direction):

        self.tempPos = self.headPos.copy()   

        if direction in self.keys.keys() and direction != self.inverseDirection:
            self.headPos[self.coordinate[direction][0]] += self.coordinate[direction][1]
            self.heading = direction       
        else:
            self.headPos[self.coordinate[self.heading][0]] += self.coordinate[self.heading][1]
   
        self.inverseDirection = self.keys[self.heading]


    def keyEvent(self, get_hotkey_name):
        
        listen = get_hotkey_name()
        if listen in list(self.keys.keys()):
           key = listen

           return key[0]   


    def checkCollision(self, scale):

        if self.headPos in self.trunk:
            return True

        for i in self.headPos:
            if i <= -1 or i >= scale:
                return True
            
        return False
