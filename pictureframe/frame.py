WIDTH=30
HEIGHT=20
FULLSCREEN=True

from time import localtime, strftime
clock = None
def update():
   global clock
   if clock:
      clock.destroy()
   background()
   clock = text(strftime("%H:%M", localtime()), color=WHITE, pos=(25, 18), size=2)
update()
callback(update, 10, repeat=FOREVER)


