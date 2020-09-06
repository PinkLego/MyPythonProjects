import tkinter
window = tkinter.Tk()
button = tkinter.Button(window, text="Do not press button", width=40)
button.pack(padx=30, pady=30)
clickCount = 0
def onClick(event):
    global clickCount
    clickCount = clickCount + 1
    if clickCount == 1:
        button.configure(text="Seriously? Do. Not. Press. It.")
    elif clickCount == 2:
        button.configure(text="STOP RIGHT THERE! DO NOT TOUCH")
    elif clickCount == 3:
        button.configure(text="I mean it!")
    elif clickCount == 4:
        button.configure(text="I'm being nice now... STOP please 😤")
    elif clickCount == 5:
        button.configure(text="🤖🤖👾👽😼😽🙀🤢🤮🥴🤪🤒😷🥶🤯😨🙄🙄😶😪🤤😴😍😎😎😎😎😎😎😎😎😎😎")
    elif clickCount == 6:
        button.configure(text="Bye-bye TRAIDOR!")
    else:
        button.pack_forget()
button.bind("<ButtonRelease-1>", onClick)
window.mainLoop()

  
