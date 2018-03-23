#splats should be in the center
import sys
name = None
if len(sys.argv) != 3:
    sys.exit('usage: pigm animation.py <actor_name>')
else:
    name = sys.argv[2]

WIDTH = 10
HEIGHT = 10
TITLE = 'Animated Actor'

a = actor(name, center=(5,5), size=8)
txt = text('IDLE', pos=(0,0), color=BLACK)
actions = a.get_actions()
action = -1

def act():
    global action
    global txt
    action += 1
    if action >= len(actions):
       action = 0
    txt.destroy()
    txt = text(actions[action].upper(), pos=(0,0), color=BLACK)
    a.act(actions[action], FOREVER)

keydown('space', act)

frame_rate = 1
def slower():
    global frame_rate
    frame_rate = frame_rate + 1
    a.rate(frame_rate)

def faster():
    global frame_rate
    frame_rate = frame_rate - 1
    a.rate(frame_rate)

keydown('=', slower)
keydown('-', faster)
