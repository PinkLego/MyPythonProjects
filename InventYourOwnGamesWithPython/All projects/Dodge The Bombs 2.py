import tkinter
import random
gameOver = False
score = 0
squaresToClear = 0
def play_bombdodger():
    create_bombfield(bombfield):
        window = tkinter.Tk()
        layout_window(window)
        window.mainloop()
bombfield = []
def create_bombfield(bombfield):
    global squaresToClear
    for row in range(0,10):
        rowList = []
        for column in range(0,10):
            if random.randint(1,100) < 20:
                rowList.append(1)
            else:
                rowList.append(0)
                squaresToclear = squaresToclear + 1
        bomfield.append(rowList)
    printfield(bombfield)
def printfield(bombfield):
    for rowlist in bombfield:
        print(rowList)
play_bombdogder()
def layout(window):
    for rowNumber, rowList in enumerate(bombfield):
        for columnNumber, columnEntry in enumerate(rowList):
            if random.randint(1,100) < 25:
                square = tkinter.Label(window, text = "    ", bg = "darkgreen")
            elif random randint(1, 100)
