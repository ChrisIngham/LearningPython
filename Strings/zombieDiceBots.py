import zombiedice, random
# roll() returns a dict with keys: 'brains', 'shotgun', and 'footsteps' with how many of each there are
# the 'rolls' key is a list of (color, icon) tuples with exact roll result info
# example: {'brains': 1, 'footsteps' : 1, 'shotgun': 1,
#           'rolls': [('yellow', 'brains'), ('red', 'footsteps'), ('green', 'shotgun')]}


# bot that after the first roll randomly picks if it will roll again
class StopsAfterFirst:
    def __init__(self, name):
        self.name = name    # all zombies must have a name
    def turn(self, gameState):
        diceRollResults = zombiedice.roll()     # first roll
        while diceRollResults is not None:
            if random.randint(0,1) == 1:
                diceRollResults = zombiedice.roll()
            else:
                break


# bot that stops rolling after it has rolled 2 brains
class TwoBrains:
    def __init__(self, name):
        self.name = name    # all zombies must have a name
    def turn(self, gameState):
        diceRollResults = zombiedice.roll()     # first roll
        while diceRollResults is not None:
            brains = 0
            brains += diceRollResults['brains']

            if brains == 2:
                break
            else:
                diceRollResults = zombiedice.roll()     #rolls again


# bot that stops rolling after it has rolled two shotguns
class TwoShotguns:
    def __init__(self, name):
        self.name = name    # all zombies must have a name
    def turn(self, gameState):
        diceRollResults = zombiedice.roll()
        while diceRollResults is not None:
            shotguns = 0
            shotguns = diceRollResults['shotgun']

            if shotguns == 2:
                break
            else:
                diceRollResults = zombiedice.roll()

# bot that initally decides it'll roll dice one to four times, but will stop early if 2 shotguns are rolled
class StopIf2Shotguns:
    def __init__(self, name):
        self.name = name    # all zombies must have a name
    def turn(self, gameState):
        diceRollResults = zombiedice.roll()
        count =0
        while diceRollResults is not None and count <4:
            shotguns = 0
            shotguns = diceRollResults['shotgun']
            if shotguns == 2:
                break
            else:
                diceRollResults = zombiedice.roll()
                count +=1

# bot that stops rolling after it has more shotguns than brains
class MoreShotgunsThanBrains:
    def __init__(self, name):
        self.name = name    # all zombies must have a name

    def turn(self, gameState):
        diceRollResults = zombiedice.roll()
        while diceRollResults is not None:
            shotguns = 0
            brains = 0
            shotguns = diceRollResults['shotgun']
            brains = diceRollResults['brains']
            if shotguns > brains:
                break
            else:
                diceRollResults = zombiedice.roll()

zombies = (
    zombiedice.examples.RandomCoinFlipZombie(name = 'Random'),
    zombiedice.examples.RollsUntilInTheLeadZombie(name = 'Until Leading'),
    zombiedice.examples.MinNumShotgunsThenStopsZombie(name = 'Stops at 2 Shotguns', minShotguns = 2),
    zombiedice.examples.MinNumShotgunsThenStopsZombie(name = 'Stops at 1 Shotun', minShotguns = 1),
    StopsAfterFirst(name= 'StopsAfterFirst'),
    TwoBrains(name= 'TwoBrains'),
    TwoShotguns(name= 'TwoShotguns'),
    StopIf2Shotguns(name='StopIf2Shotguns'),
    MoreShotgunsThanBrains(name='MoreShotgunsThanBrains')

)

#zombiedice.runTournament(zombies=zombies, numGames=1000)
zombiedice.runWebGui(zombies = zombies, numGames= 1000)