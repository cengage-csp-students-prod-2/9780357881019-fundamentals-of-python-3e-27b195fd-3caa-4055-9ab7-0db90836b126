import breezypythongui
from time import sleep

class Window(breezypythongui.EasyFrame):
    """The window for the number guesser."""
    
    def __init__(self):
        """
        Creates the main window and its widgets.
        """
        
        breezypythongui.EasyFrame.__init__(self, "Number guesser")
        self.promptlabel=self.addLabel("Let's play. Think up a number between 0 and 100.", 0, 0,columnspan=3)
        self.readybutton=self.addButton("READY",1,0,columnspan=3,command=self.startgame)
        self.maxvalue=100
        self.minvalue=0
    def guess(self):
        """
        Computes the next guess and displays it in the window.
        The computation is done by taking the average of the current
        minvalue and maxvalue. The result is displayed in the window
        after a short delay.
        """
        self.promptlabel.configure(text="Thinking....")
        self.update()
        sleep(0.5)
        self.guessednumber=(self.maxvalue+self.minvalue)//2
        self.promptlabel.configure(text="My guess is "+str(self.guessednumber))#+f' min {self.minvalue} max {self.maxvalue} ') 
    def startgame(self):
        """
        Destroys the 'Ready' button and creates three new buttons,
        TOO SMALL, TOO BIG and CORRECT, and starts the game by calling
        the guess method.
        """
        self.readybutton.destroy()
        self.toosmallbutton=self.addButton("TOO SMALL",1,0,command=self.toosmall)
        self.toobigbutton=self.addButton("TOO BIG",1,1,command=self.toobig)
        self.correctbutton=self.addButton(">>CORRECT<<",1,2,command=self.correct)
        self.guess()
    def restart(self):
        """
        Resets the game to its initial state by removing the game buttons
        and recreating the 'Ready' button. The prompt is reset, and the
        minvalue and maxvalue are restored to their default values.
        """

        self.toosmallbutton.destroy()
        self.toobigbutton.destroy()
        self.correctbutton.destroy()
        self.readybutton=self.addButton("READY",1,0,columnspan=3,command=self.startgame)
        self.promptlabel.configure(text="Let's play. Think up a number between 0 and 100.")
        self.maxvalue=100
        self.minvalue=0
    def toosmall(self):
        """
        Handles the event when the user clicks the TOO SMALL button.
        Adjusts the minvalue and checks if the user has lied, in which case
        the game is restarted. Otherwise, the game continues with the
        next guess.
        """
        self.minvalue=self.guessednumber+1
        if self.maxvalue<self.minvalue:
            self.messageBox("Error","You lied to me at least once, let's start over")
            self.restart()
            return
        self.guess()
    def toobig(self):
        """
        Handles the event when the user clicks the TOO BIG button.
        Adjusts the maxvalue and checks if the user has lied, in which case
        the game is restarted. Otherwise, the game continues with the
        next guess.
        """
        self.maxvalue=self.guessednumber-1
        if self.maxvalue<self.minvalue:
            self.messageBox("Error","You lied to me at least once, let's start over")
            self.restart()
            return
        self.guess()
    def correct(self):
        """
        Handles the event when the user clicks the CORRECT button.
        Displays a messagebox with a success message and restarts the game.
        """
        self.messageBox("Hurrah!","That's it! I guessed "+str(self.guessednumber)+"\nYes, I use binary search")
        self.restart()

Window().mainloop()