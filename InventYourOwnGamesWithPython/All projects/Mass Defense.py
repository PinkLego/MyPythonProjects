#
#
#
#

import turtle
import random

wn = turtle.Screen()
wn.setup(1200, 800)
wn.bgcolor("black")
wn.title("Mass Defense Game")

class Sprite():

    pen  = turtle.Turtle()
    pen.hideturtle()
    pen.speed(0)
    pen.penup()

    def __init__(self, x, y, shape, color):
        self.x = x
        self.y = y
        self.shape = shape 
        self.color = color
        self.dx = 0
        self.speed = 0

    def render(self):
        Sprite.pen.goto(self.x, self.y)
        Sprite.pen.shape(self.shape)
        Sprite.pen.color(self.color)
        Sprite.pen.stamp()

    def move(self):
        self.x += self.dx

sprites = []

#Defenders
for _ in range(10):
    x = random.randint(-500, -300)
    y = random.randint(-300, 300)
    sprites.append(Sprite(x, y, "circle", "blue"))

# Attackers
for _ in range(10):
    x = random.randint(300, 500)
    y = random.randint(-300, 300)
    sprites.append(Sprite(x, y, "circle", "red"))
    sprites[-1].heading = 180 #Left
    sprites[-1].dx = -0.2

# Weapons
for _ in range(10):
    x = -1000
    y = -1000
    sprites.append(Sprite(x, y, "circle", "light blue"))

# Main game loop
while True:

    # Move
    for sprite in sprites:
        sprite.move()

    #Render
    for sprite in sprites:
        sprite.render()

    # Update the screen
    wn.update()

    # Clear the screen
    Sprite.pen.clear()


wn.mainloop()
