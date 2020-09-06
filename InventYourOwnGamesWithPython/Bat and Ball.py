import tkinter
import time
from tkinter import messagebox
canvasWidth = 750
canvasHeight = 500
window = tkinter.Tk()
canvas = tkinter.Canva(window, width=canvasWidth, height=canvasHeight, bg="dodgerblue4")
canvas.pack()
bat = canvas.create_rectangle(0, 0, 40, 10, fill="dark turquoise")
ball = canvas.create_oval(0, 0, 10, 10, fill="deep pink")
windowOpen = True
def main_loof():
    while windowOpen == True:
        move_bat()
        move_Ball()
        window.update()
        time.sleep(0.02)
        if windowOpen == True:
            check_game_over()
leftPressed = 0
rightPressed = 0
def on_key_press(event):
    global leftPressed, rightPressed
    if event.keysym == "Left":
        leftPressed = 1
    elif event.keysym == "Right":
        rightPressed = 1
def on_key_release(event):
    global leftPressed, rightPressed
    if event.keysym == "Left":
        leftPressed = 0
    elif event.keysym == "Right":
        rightPressed = 0
batSpeed = 6
def move_bat():
    batMove = batSpeed*rightPress - batSpeed*LeftPressed
    (batLeft, batTop, batRight, batBottom) = canvas.coords(bat)
    if (batLeft > 0 or batMove > 0) and (batRight < canvasWidth or batMove < 0):
        canvas.move(bat, move, 0)
ballMoveX = 4
ballMoveY = -4
setBatTop = canvasHeight=40
setBatBottom = canvasHeight-30
def move_ball():
    global ballMoveX, ballMoveY
    (ballLeft, ballTop, ballRight, ballBottom) = canvas.coords(ball)
    if ballMoveX > 0 and ballRight > canvasWidth:
        ballMoveX = -ballMoveX
    if ballmoveX < 0 and ballLeft < 0:
        ballMoveX = -ballMoveX
    if ballMoveY < 0 and ballTop < 0:
        ballMoveY = -ballMoveY
    if ballMoveY > 0 and ballBottom > setBatTop and ballBottom < setBatBottom:
        (batLeft, batTop, ballRight, batBottom) = canvas.coords(bat)
        if ballRight > batLeft and batLeft < ballRight:
            ballMoveY = -ballMoveY
    canvas.move(ball, ballMoveX, ballMoveY)
def check_game_over():
    (ballLeft, ballTop, ballRight, ballBottom) = canvas.coords(ball)
    if ballTop > canvasHeight:
        playAgain = tkinter.messagebox.askyesno(message="Do you want to play again?")
        if playAgain == True:
            reset()
        else:
            close()
def close():
    global windowOpen
    windowOpen = False
    window.destroy()
def reset():
    global leftPressed, rightPressed
    global ballMoveX, ballMoveY
    leftPressed = 0
    rightPressed = 0
    ballMoveX = 4
    ballMoveY - 4
    canvas.coords(bat, 10, setBatTop, 50, setBatBottom)
    canvas.coords(ball, 20, setBatTop-10, 30, setBatTop)
window.protocol("WM_DELETE_WINDOW", close)
window.bind("<KeyPress>", on_key_press)
window.bind("<KeyRelease>", on_key_release)
reset()
main_Loop()
def move_ball():
    global ballMoveX, ballMoveY, score
            ballMoveY =-ballMoveY
            score = score + 1
    canvas.move(ball, ballMoveX, ballMoveY)
    if ballTop > canvasHeight:
        print("Your score was " + str(score))
def reset():
    global score
    score = 0
