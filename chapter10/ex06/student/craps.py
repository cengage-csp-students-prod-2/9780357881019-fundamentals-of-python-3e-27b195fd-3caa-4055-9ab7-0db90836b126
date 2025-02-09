"""
File: craps.py

This module studies and plays the game of craps.
"""

from die import Die

class Player(object):

    def __init__(self):
        """Has a pair of dice and an empty rolls list."""
        self.die1 = Die()
        self.die2 = Die()
        self.rolls = []
        self.roll:str=None
        self.rollsCount=0
        self.atStartup=True
        self.winner=False
        self.loser=False
    def isWinner(self):
        return self.winner

    def isLoser(self):
        return self.loser
    
    def getNumberOfRolls(self):
        return self.rolls
    
    def rollDice(self):
        self.atStartup=False
        self.rollsCount+=1

        self.die1.roll()
        self.die2.roll()
        self.roll=f'{self.die1.getValue()}+{self.die2.getValue()}'
        self.rolls.append(self.roll)
        print(self.rolls)
        return (self.die1.getValue(), self.die2.getValue())

    def __str__(self):
        """Returns a string representation of the list of rolls."""
        result = ""
        for (v1, v2) in self.rolls:
            result = result + str((v1, v2)) + " " +\
                     str(v1 + v2) + "\n"
        return result

    def getNumberOfRolls(self):
        """Returns the number of the rolls."""
        return len(self.rolls)

    def play(self):
        """Plays a game, saves the rolls for that game, 
        and returns True for a win and False for a loss."""
        
        input("Throw the dice...")
        self.rolls=[]
        self.rollDice()
        initialSum = self.die1.getValue() + self.die2.getValue()
        if initialSum in (2, 3, 12):
            self.loser=True
            #print("You lose!")
            return
        elif initialSum in (7, 11):
            #print("You win!")
            self.winner=True
            return
        while (True):
            input(f"You have {initialSum}. Throw the dice...")
            self.rollDice()
            laterSum = self.die1.getValue() + self.die2.getValue()
            if laterSum == 7:
                self.loser=True
                #print("You lose!")
                return
            elif laterSum == initialSum:
                #print("You win!")
                self.winner=True
                return

def playOneGame():
    """Plays a single game and prints the results."""
    player = Player()
    print(player)
    if player.isLoser():
        print("You lose!")
    elif player.isWinner():
        print("You win!")

def playManyGames(number):
    """Plays a number of games and prints statistics."""
    wins = 0
    losses = 0
    winRolls = 0
    lossRolls = 0
    if number < 1: return
    player = Player()
    for count in range(number):
        hasWon = player.play()
        print(player.rolls)
        rolls = player.getNumberOfRolls()
        if hasWon:
            wins += 1
            winRolls += rolls
        else:
            losses += 1
            lossRolls += rolls
    print("The total number of wins is", wins)
    print("The total number of losses is", losses)
    if wins>0: print("The average number of rolls per win is %0.2f" % \
          (winRolls / wins))
    if losses>0: print("The average number of rolls per loss is %0.2f" % \
          (lossRolls / losses))
    print("The winning percentage is %0.3f" % (wins / number))

def main():
    """Plays a number of games and prints statistics."""
    number = int(input("Enter the number of games: "))
    playManyGames(number)

if __name__ == "__main__":
    main()