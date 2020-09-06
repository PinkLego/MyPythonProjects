
import tkinter
colours = ["blue", "purple", "cyan", "white", "yellow", "green", "orange"]
def snowflake():
    for x in range(0,6):
        colors(random.choice(colours))
        snowflakeArm()
        right(60)
