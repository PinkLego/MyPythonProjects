#
#

import os
import random

# import the turtle module
import turtle
# Required by macOSX to show the window
turtle.fd(0)
# Set the animation speed to the maximum
turtle.speed(0)
# change the background color
turtle.bgcolor("black")
#Hide the default turtle
turtle.ht()
# This saves memory
turtle.setundobuffer(1)
#Speeds up drawing
turtle.tracer(1)

class Sprite(turtle.Turtle):
    def __init__(self, spriteshape, color, startx, starty):
        turtle.Turtle.__init__(self, shape = spriteshape)
        self.speed(0)
        self.penup()
        self.color(color)
        self.fd(0)
        self.goto(startx, starty)
        self.speed = 1

    def move(self):
        self.fd(self.speed)

class Player(Sprite):
    def __init__(self, spriteshape, color, startx, starty):
        Sprite.__init__(self, spriteshape, color, startx, starty)
        self.speed = 4
        self.lives = 3
    
    def turn_left(self):
        self.lt(45)

    
# Create my sprites
player = Sprite("triangle", "white", 0, 0)




# Main game loop
while True:
    player.move()
    player.turn_left()





delay = input("Press enter to finish. >")