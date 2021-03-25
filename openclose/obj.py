import random

class ai:
    def __init__(self):
        self.isPredictor = None
        self.moveInput = ""
        self.moveList=['C', 'O']
    def randMove(self):
            move1=random.randint(0,1)
            move2=random.randint(0,1)
            return (""+self.moveList[move1]+self.moveList[move2])
    def randPrediction(self):
            return(str(random.randint(0,4)))
#------------------------    
class player:    
    def __init__(self):
        self.isPredictor = None
        self.moveInput = ""