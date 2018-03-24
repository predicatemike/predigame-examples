Keeping Score
===========
Every game needs a way to keep score. This examples showcases a few of the current scoring options that are included in Predigame. While it's always possible to write your own scoring code, we've found these options cover many common use cases.

To get started, let's create a file `score.py`. For the code, we'll start by defining our screen dimensions (30 x 20 grid cells) and provide a title.

```python
WIDTH = 30
HEIGHT = 20
TITLE = 'Scoring Demo'
```
# Accumulator
The first score box we'll define will go to the upper left corner of the screen.
```python
score(color=WHITE)
```
You can try running your game now and you'll notice the scoring box. Without any options, the *default* scoring box is a simple numeric score counter.

```
my_machine$ pred score.py
```
# Value
The next score box is a numeric value holder. Unlike the previous example, this score box will not count the score, but rather display a value.

```python
score(pos=UPPER_RIGHT, method=VALUE)
```

# Timer (countdown)
Some games may have a countdown timer where the player must complete an operation within a designated amount of time. This example adds a `timer()` callback function that is executed when the value reaches the goal of `0`.

```python
# a callback used for a timer
def timer():
   text('GAME OVER')
   gameover()

# position this scoreboard in the bottom right corner
# run as a timer from 30 to 0 (step is -1 so the counter "steps down")
# when the goal of 0 is reached, execute the timer callback function
score(30, pos=LOWER_RIGHT, method=TIMER, step=-1, goal=0, callback=timer, prefix='Time Left:')
```
# Timer (duration)
Similar to the countdown timer, is a duration timer that displays the amount time the player has been playing the game (or level). As with the countdown timer, it is possible to define a `goal` and a callback, but we elect to simply show the time.

```python
# position this scoreboard in the bottom left corner
# run as a timer from 0 to 10 (the goal), in increments of 1
# add a prefix "Duration:"
# since there is no callback registered, the counter will simply when the goal is obtained
score(pos=LOWER_LEFT, method=TIMER, step=1, goal=10, prefix='Duration:')
```

# A Silly Scoring Example
To showcase all of our scoring boxes in operation, let's create a simple circle clicking game. Here's the complete version that also includes the previously defined timers.

```python
WIDTH = 30
HEIGHT = 20
TITLE = 'Scoring Demo'

# default scoring box (upper left corner)
score(color=WHITE)

# place this scoreboard in the upper right corner and just show the value
# this means the scoreboard will not accumulate the score
score(pos=UPPER_RIGHT, method=VALUE)

# position this scoreboard in the bottom left corner
# run as a timer from 0 to 10 (the goal), in increments of 1
# add a prefix "Duration:"
# since there is no callback registered, the counter will simply when the goal is obtained
score(pos=LOWER_LEFT, method=TIMER, step=1, goal=10, prefix='Duration:')

# a callback used for a timer
def timer():
   text('GAME OVER')
   gameover()

# position this scoreboard in the bottom right corner
# run as a timer from 30 to 0 (step is -1 so the counter "steps down")
# when the goal of 0 is reached, execute the timer callback function
score(30, pos=LOWER_RIGHT, method=TIMER, step=-1, goal=0, callback=timer, prefix='Time Left:')

# a simple sprite callback for popping circles and executing the score Options
# every three pops will reset the scoreboard in the upper right corner
def pop(s):
   s.destroy()
   score(1)
   score(100, pos=UPPER_RIGHT)
   if score() % 3 == 0:
      reset_score(pos=UPPER_RIGHT, method=VALUE)

# silly circle drawer
def show():
   shape(CIRCLE, RED).clicked(pop)
   callback(show, rand(0,2))
callback(show, 0.5)

# register a 'r' keydown method to reset
keydown('r', reset)
```

