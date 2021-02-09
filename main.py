from tkinter import *
import tkinter.font as tkFont



class App(Tk):
    def __init__(self):
        Tk.__init__(self)
        self.geometry("300x400+100+100")
        self.titlefont = tkFont.Font(family="Arial", size=20, slant="italic")
        self.buttonfont = tkFont.Font(family="Arial", size=16)
        self.statusfont = tkFont.Font(family="Consolas", size=14)
        lab1 = Label(self, text="Hexapawn", font=self.titlefont)
        lab1.grid(row=0, column=0, sticky=W, columnspan=2)

        self.theCanvas =Canvas(self, width=300,height = 300, bg="#fffed6")
        self.theCanvas.grid(row=1, column=0, columnspan=2)

        self.statusText = Label(self, text="Pick a number of players", font=self.statusfont, fg="blue")
        self.statusText.grid(row=2, column=0, columnspan=2, sticky="W")
        self.OnePlayerButton = Button(self,text="1 player", font = self.buttonfont, command = lambda players=1:self.setPlayers(players))
        self.TwoPlayerButton = Button(self,text="2 players", font = self.buttonfont, command = lambda players=2:self.setPlayers(players))
        self.OnePlayerButton.grid(row=3,column=0, sticky="NSEW")
        self.TwoPlayerButton.grid(row=3,column=1, sticky="NSEW")
        self.gameState = self.newGame()


        self.theCanvas.bind("<Button-1>", self.canvasClicked)

        self.mainloop()


    def newGame(self):
        # starts a new game and returns the new opening game state
        self.OnePlayerButton.grid(row=3,column=0, sticky="NSEW") # bring the buttons back
        self.TwoPlayerButton.grid(row=3,column=1, sticky="NSEW")
        self.currentPlayer = 0 # no current player
        self.drawCanvas()
        return [ ["B","B","B"], ["","",""], ["W","W","W"] ]

    def setPlayers(self,players):
        self.numplayers = players
        self.OnePlayerButton.grid_forget()
        self.TwoPlayerButton.grid_forget()
        self.statusText.config(text="Take your turn, Player 1")
        self.currentPlayer = 1


    def canvasClicked(self,e):
        print(e.x, e.y)

    def drawCanvas(self):
        self.theCanvas.delete("ALL")
        self.theCanvas.create_line(0,100,300,100) # draw the lines of the grid
        self.theCanvas.create_line(0,200,300,200)
        self.theCanvas.create_line(100,0,100,300)
        self.theCanvas.create_line(200,0,200,300)


app = App()