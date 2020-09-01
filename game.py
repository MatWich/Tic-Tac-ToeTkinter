from tkinter import *
from config import *
from player import *

class Game:
    def __init__(self, clicked):
        self.clicked = clicked  # Who starts firsts [Boolean]
        self.count = 0  # if reaches 9 game tie     [Integer]
        self.title = TITLE
        self.screen = Tk()
        self.players = [Player("X", 0), Player("O", 0)]
        self.player1Score = IntVar()
        self.player2Score = IntVar()
        
    def setUp(self):
        pass

    def mainLoop(self):
        self.screen.mainloop()
    
    def setUpWindow(self):
        self.screen.title(self.title)
        self.screen.geometry("1350x750+0+0")
        self.screen.configure(background="Light Yellow")
        self.CreateLayout()
        self.CreateBoard()
        self.CreateOptions()

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

    def CreateBoard(self):
        
        # Row 1
        button1 = Button(self.LeftFrame, text = " ", font=('Times', 26, 'bold'), height=3, width=8, bg='gainsboro', command=lambda: self.click(button1))
        button1.grid(row=1, column=0, sticky=N+S+E+W)

        button2 = Button(self.LeftFrame, text = " ", font=('Times 26 bold'), height=3, width=8, bg='gainsboro', command=lambda: self.click(button2))
        button2.grid(row=1, column=1, sticky=N+S+E+W)

        button3 = Button(self.LeftFrame, text = " ", font=('Times 26 bold'), height=3, width=8, bg='gainsboro', command=lambda: self.click(button3))
        button3.grid(row=1, column=2, sticky=N+S+E+W)

        # ROW 2
        button4 = Button(self.LeftFrame, text = " ", font=('Times 26 bold'), height=3, width=8, bg='gainsboro', command=lambda: self.click(button4))
        button4.grid(row=2, column=0, sticky=N+S+E+W)

        button5 = Button(self.LeftFrame, text = " ", font=('Times 26 bold'), height=3, width=8, bg='gainsboro', command=lambda: self.click(button5))
        button5.grid(row=2, column=1, sticky=N+S+E+W)

        button6 = Button(self.LeftFrame, text = " ", font=('Times 26 bold'), height=3, width=8, bg='gainsboro', command=lambda: self.click(button6))
        button6.grid(row=2, column=2, sticky=N+S+E+W)

        # ROW 3
        button7 = Button(self.LeftFrame, text = " ", font=('Times 26 bold'), height=3, width=8, bg='gainsboro', command=lambda: self.click(button7))
        button7.grid(row=3, column=0, sticky=N+S+E+W)

        button8 = Button(self.LeftFrame, text = " ", font=('Times 26 bold'), height=3, width=8, bg='gainsboro', command=lambda: self.click(button8))
        button8.grid(row=3, column=1, sticky=N+S+E+W)

        button9 = Button(self.LeftFrame, text = " ", font=('Times 26 bold'), height=3, width=8, bg='gainsboro', command=lambda: self.click(button9))
        button9.grid(row=3, column=2, sticky=N+S+E+W)

        self.buttons = [button1, button2, button3, button4, button5, button6, button7, button8, button9]

    # onclick for button
    def click(self, button):
        pass
    
    # Clear up board
    def reset(self):
        pass

    # reset but with clearing the scores :D
    def newGame(self):
        pass

    def CreateOptions(self):
        '''Reset button, new game button and Scores'''

        lblPlayerX = Label(self.RightFrame1, font=('arial',40,'bold'),padx=2, pady=2, text="Player : " + self.players[0].sign, bg="Light Yellow")
        lblPlayerX.grid(row=0, column=0, sticky=W)

        txtPlayerX=Entry(self.RightFrame1, font=('arial',40,'bold'), bd=2, fg="black", textvariable= self.player1Score, width=14, justify=LEFT)
        txtPlayerX.grid(row=0, column=1)

        lblPlayerO = Label(self.RightFrame1, font=('arial',40,'bold'),padx=2, pady=2, text="Player : " + self.players[1].sign, bg="Light Yellow")
        lblPlayerO.grid(row=1, column=0, sticky=W)
        
        txtPlayerO=Entry(self.RightFrame1, font=('arial',40,'bold'), bd=2, fg="black", textvariable= self.player2Score, width=14, justify=LEFT)
        txtPlayerO.grid(row=1, column=1)
        
        btnReset = Button(self.RightFrame2, text = "Restart", font=('arial',40,'bold'), height=1, width=20, bg='gainsboro', command=self.reset)
        btnReset.grid(row=2, column=0, padx=6, pady=10)

        btnNew = Button(self.RightFrame2, text = "New Game", font=('arial',40, 'bold'), height=1, width=20, bg='gainsboro', command=self.newGame)
        btnNew.grid(row=3, column=0, padx=6, pady=10)