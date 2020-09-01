from tkinter import *
from config import *

class Game:
    def __init__(self, clicked):
        self.clicked = clicked  # Who starts firsts [Boolean]
        self.count = 0  # if reaches 9 game tie     [Integer]
        self.title = TITLE
        self.screen = Tk()
        
    def setUp(self):
        pass

    def mainLoop(self):
        self.screen.mainloop()
    
    def setUpWindow(self):
        self.screen.title(self.title)
        self.screen.geometry("1350x750+0+0")
        self.screen.configure(background="Black")