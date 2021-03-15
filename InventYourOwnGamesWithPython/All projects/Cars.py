command = ""
started = False
while True:
    command = input("> ").lower()
    if command == "start":
        # If the command is start the car should start.
        print("Car started...!")
    elif command == "stop":
        if not started:
            print("Car is already stopped!😤")
        else:
            started = True
        # If the command is stop the car should stop.
        print("Car stopped.")
    elif command == "help":
        print("""
start - start the car
stop - stop the car
quit - exit the car
        """)
    elif command == "quit":
        break
    else:
        print("Sorry I don't understand that!")