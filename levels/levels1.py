# This is a simple game with two levels
WIDTH = 30
HEIGHT = 20
TITLE = 'Simple Two Level Example'

# hold a reference to the current level
current_level = None

# support functions used in every level
def pop(s):
    # destroy the circle
    s.destroy()
    # tally the hit
    current_level.hit()

class PopLevel1(Level):
    def __init__(self, duration):
        self.hits = 0
        self.duration = duration

    def hit(self):
        # update the number of hits
        self.hits += 1

        # refresh the score
        score(self.hits)

    def get_duration(self):
        return score(pos=LOWER_RIGHT)

    def setup(self):
        """ setup the level """

        # Hold a reference to this level
        global current_level
        current_level = self

        # create one target at a random location
        shape(CIRCLE).clicked(pop)

        # SCORE BOARD
        score(0, color=BLACK, method=VALUE, prefix='Hits: ')
        score(pos=LOWER_RIGHT, color=BLACK, value=self.duration, method=TIMER,
              step=1, goal=1000, prefix='Duration: ')

        # KEYBOARD EVENTS
        keydown('r', reset)

    def completed(self):
        """ level is complete when all targets have been destroyed """
        # completed if one circle clicked
        if self.hits == 1:
            return True
        else:
            return False

    def next(self):
        """ load the next level """
        # preserve the time
        return PopLevel2(duration=score(pos=LOWER_RIGHT))

class PopLevel2(Level):
    def __init__(self, duration):
        self.hits = 0
        self.duration = duration

    def hit(self):
        # update the number of hits
        self.hits += 1

        # refresh the score
        score(self.hits)

    def get_duration(self):
        return score(pos=LOWER_RIGHT)

    def setup(self):
        """ setup the level """

        # Hold a reference to this level
        global current_level
        current_level = self

        # create two circles at random locations
        shape(CIRCLE).clicked(pop)
        shape(CIRCLE).clicked(pop)

        # SCORE BOARD
        score(0, color=BLACK, method=VALUE, prefix='Hits: ')
        score(pos=LOWER_RIGHT, color=BLACK, value=self.duration, method=TIMER,
              step=1, goal=1000, prefix='Duration: ')

        # KEYBOARD EVENTS
        keydown('r', reset)

    def completed(self):
        """ level is complete when all targets have been destroyed """
        # completed if two circles clicked
        if self.hits == 2:
            return True
        else:
            return False

    def next(self):
        """ end the game.. there is no next level """
        text("YOU SOLVED ALL LEVELS!")
        gameover()

# start the game at level 1
level(PopLevel1(1))
