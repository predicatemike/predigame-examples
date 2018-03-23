Levels
===========
Predigame utilizes [Python Classes](https://docs.python.org/3/tutorial/classes.html) to implement a game with levels. If you're new to the *class abstraction* be sure to click on the previous link and learn about a pretty cool way of organizing your code.  

A Predigame level consists of three key ingredients:

1. a `setup()` member containing any code that should run prior to the start of a given level.
2. a `completed()` member that assesses if a given objective has been established.
3. a `next()` member that instructs Predigame the next level to load.

With that in mind, let's take a look at two mini-game examples.

# Example 1: Statically Defined Levels

This example is pretty basic. We introduce game with two statically defined levels - level 1 draws one circle, level 2 draws two circles. Yup. Pretty basic, but it illustrates the mechanics of what it takes to create a level.

```python
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
```
# Example 2: Dynamic Levels

This example builds on the previous but now increases the number of circles that are drawn with each level. We've also introduced a countdown timer. The objective of this game is to see how many levels the player can reach by clicking all circles within `10` seconds. You'll notice that there is much less code in this examples. Dynamic levels are fun!

```python
# Create a basic game that demonstrates how to create levels
# In each level, the player has to pop all the circles in 10 seconds
# A new circle will be added for each level

WIDTH = 30
HEIGHT = 20
TITLE = 'Simple Levels Example'

current_level = None

def timer():
    text("You survived " + str(current_level.get_duration()) + " seconds.")
    gameover()
 
def pop(s):
    s.destroy()
    current_level.hit()

class PopLevel(Level):
    def __init__(self, level=1, duration=0):
        self.level = level
        self.hits = 0
        self.time_remaining = 10
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

        # TARGETS
        for x in range(self.level):
            shape(CIRCLE).clicked(pop)

        # SCORE BOARD
        score(0, color=BLACK, method=VALUE, prefix='Hits: ')
        score(pos=LOWER_LEFT, color=BLACK, value=self.time_remaining, method=TIMER,
              step=-1, goal=0, callback=timer, prefix='Time Remaining: ')
        score(pos=LOWER_RIGHT, color=BLACK, value=self.duration, method=TIMER,
              step=1, goal=1000, prefix='Duration: ')
        score(self.level, pos=UPPER_RIGHT, color=BLACK, method=VALUE, prefix='Level: ')

        # KEYBOARD EVENTS
        keydown('r', reset)

    def completed(self):
        """ level is complete when all targets have been destroyed """
        if self.hits == self.level:
            return True
        else:
            return False

    def next(self):
        """ load the next level """
        return PopLevel(level=self.level+1, duration=score(pos=LOWER_RIGHT))

level(PopLevel(1))

```


