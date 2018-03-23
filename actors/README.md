Actor Framework
===================
Predigame Actors are Sprites that perform certain **actions** - mostly in the form of animations that make the game more realistic. Actors can perform any number of actions (walk, run, jump, attack) which are usually left up to the artist's creation of the sprite.

Here are a few example Actors.

![alt text](http://predicate.us/predigame/images/zombie_animated.gif "Predigame Zombies")

![alt text](http://predicate.us/predigame/images/other_animated.gif "Predigame Actors")


## Asset Licenses

All static artwork has been obtained from  [OpenGameArt](https://opengameart.org/)  or from Google with the "Labeled for reuse" filtered defined. Animated sprites are licensed to Predicate Academy (Predigame's developer) for use limited to non-commercial Predigame development.


# How Actors Work
The artwork we use for actors are *four directional sprites* in that each of the actions are repeated in each direction of movement (up, down, left, right). Actor animations may seem a bit complicated under the hood, but it is nothing more than just a sequence of still images that are refreshed at a fast enough rate to give the **illusion of animation**.

In Predigame we store actors as **.pga** files in the `actors` directory. Every **.pga** file of actions and directions as highlighted in the picture below:
![alt text](http://predicate.us/predigame/images/actors.png "Predigame Actors ")

Each of the highlighted png files capture a single frame.
![alt text](http://predicate.us/predigame/images/actors2.png "Predigame Actors ")

And when those frames are rotated fast enough the actor (in this case the zombie) appears to be attacking! Pretty cool, right?

Now let's explore some animations. We provided a simple animation utility that enumerates through all possible animations for a given actor (just hit the space bar). Here's a few examples for running this utility:

```
my_machine$ pigm animation.py Bee
my_machine$ pigm animation.py Skeleton
my_machine$ pigm animation.py Soldier-1
my_machine$ pigm animation.py Viking
my_machine$ pigm animation.py Witch
my_machine$ pigm animation.py Zombie-1
```
