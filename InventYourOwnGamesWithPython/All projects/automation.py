#
#
#
#

import turtle
import random

wn = turtle.Screen()
wn.setup(800, 400)
wn.bgcolor("black")
wn.title("Mass Defense Game")

class Sprite():

    pen  = turtle.Turtle()
    pen.hideturtle()
    pen.speed(0)

    def __init__(self, x, y, shape):
        self.x = x
        self.y = y
        self.shape = shape 
        self.color = color

    def render(self):
        Sprite.pen.goto(self.x, self.y)
        Sprite.pen.shape(self.shape)
        Sprite.pen.color(self.color)
        Sprite.pen.stamp()

sprites = []

#Defenders
for _ in range(10):
    x = random.randint(-500, -300)
    y = random.randint(-300, 300)
    sprites.append(Sprite(x, y, "circle", "blue"))

# Attackers


# Main game loop
while True:
    #Render
    for sprites in sprites:
        sprite.render()


wn.mainloop()
