class Player:
    def __init__(self, sign, score):
        self.score = score
        self.sign = sign
    
    def setZeroScore(self):
        self.score = 0