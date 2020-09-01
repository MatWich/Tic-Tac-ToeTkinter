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
        self.screen.configure(background="Light Yellow")
        self.CreateLayout()

    def CreateLayout(self):
        self.Tops = Frame(self.screen, bg="Light yellow", pady=2, width=1350, height=100, relief=SUNKEN)
        self.Tops.grid(row=0, column=0)

        self.lblTitle = Label(self.screen, font=('arial',50,'bold'), text=TITLE, bd=21, bg="Light Yellow", fg="Black", justify=CENTER)
        self.lblTitle.grid(row=0, column=0)

        self.MainFrame = Frame(self.screen, bg="Light Yellow", pady=2, width=1350, height=600, relief=SUNKEN)
        self.MainFrame.grid(row=1, column=0)

        self.LeftFrame = Frame(self.MainFrame, bd=10, width=750, height=500, pady=2, padx=10, bg="Light Yellow", relief=SUNKEN)
        self.LeftFrame.pack(side=LEFT)

        self.RightFrame = Frame(self.MainFrame, bd=10, width=560, height=500, pady=2, padx=10, bg="Light Yellow", relief=SUNKEN)
        self.RightFrame.pack(side=RIGHT)

        self.RightFrame1 = Frame(self.RightFrame, bd=10, width=560, height=200, pady=2, padx=10, bg="Light Yellow", relief=SUNKEN)
        self.RightFrame1.grid(row=0, column=0)

        self.RightFrame2 = Frame(self.RightFrame, bd=10, width=560, height=200, pady=2, padx=10, bg="Light Yellow", relief=SUNKEN)
        self.RightFrame2.grid(row=1, column=0)