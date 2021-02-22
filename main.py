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

        self.theCanvas.bind("<Button-1>", self.canvasClicked)
        self.newGame()
        self.mainloop()


    def newGame(self):
        # starts a new game and returns the new opening game state
        self.OnePlayerButton.grid(row=3,column=0, sticky="NSEW") # bring the buttons back
        self.TwoPlayerButton.grid(row=3,column=1, sticky="NSEW")
        self.currentPlayer = 0 # Game has not started
        self.boardState = [ ["B","B","B"], ["","B",""], ["W","W","W"] ]
        self.drawCanvas()

    def setPlayers(self,players):
        self.numplayers = players
        self.OnePlayerButton.grid_forget()
        self.TwoPlayerButton.grid_forget()
        self.statusText.config(text="Take your turn, Player 1")
        self.currentPlayer = 1
        self.movestate = 1 # this means "waiting for the start position of the move"

    def gameWon(self, playerNum):
        # this should check the board ( self.boardState) to see if the player
        # in question has won the game.
        # Does their opponent have no pieces left?
        # or does this player have a piece on the final row?
        # If so, return True, else False
        pass

    def canvasClicked(self,e):
        # work out which row and column has been clicked.
        # based on e.x and e.y
        rowclicked = 0  # change this
        colclicked = 0
        if self.currentPlayer == 0:
            # game has not started  
            print(rowclicked, colclicked) # just print the position that was clicked
        elif self.currentPlayer == 1:
            if self.movestate == 1:
                # this is the start of player 1's move
                # see if that's a valid square (does it contain a white piece?)
                # if not, update the statustext: self.statusText.config(text="Select one of your pieces")

                # if it's valid, remember this starting row and column,
                # then ask for the destination square 
                # and set self.movestate to 2
                pass
            if self.movestate == 2:
                # player 1 has just clicked a destination square
                # see if it's valid, either:
                #    one square ahead and empty or
                #    diagonal and occupied by an enemy piece
                # if not valid, update status test
                # if so, move the piece. Update the board array, redraw the board

                # check to see if they have won the game!
                # if not, change self.currentPlayer to 2
                # set self.movestate to 1
                # update status text and get ready for player 2 move
                pass
        elif self.currentPlayer == 2:
            if self.movestate == 1:
                # same for player 2, but it is moving in the other direction
                pass
            elif self.movestate == 2:
                # same for player 2, but it is moving in the other direction
                pass        

    def drawCanvas(self):
        self.theCanvas.delete("ALL")
        self.theCanvas.create_line(0,100,300,100) # draw the lines of the grid
        self.theCanvas.create_line(0,200,300,200)
        self.theCanvas.create_line(100,0,100,300)
        self.theCanvas.create_line(200,0,200,300)
        for row in range(3):
            for col in range(3):
                # look at the board array and draw pieces where they appear
                if self.boardState[row][col]=="B":
                    self.theCanvas.create_oval(col*100+10, row*100+10, col*100+90, row*100+90, fill="black")
                if self.boardState[row][col]=="W":
                    self.theCanvas.create_oval(col*100+10, row*100+10, col*100+90, row*100+90, fill="white")
app = App()