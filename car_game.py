# CAR GAME

print("WELCOME TO HOUND'S CAR GAME\n\nEnter \"Help\" for instructions\n")

enter_command = ""
started = False

while True:
    enter_command = input(">> ").lower()

    if enter_command == "start":
        if started:
            print("Car is already started")
        else:
            started = True
            print("Car started... Ready to move")
    elif enter_command == "stop":
        if not started:
            print("Car is already stopped. Enter \"start\" to start moving")
        else:
            started = False
            print("Car stopped.")
    elif enter_command == "quit":
        print("Thank you for playing.")
        break
    elif enter_command == "help":
        print("""
Start - To start moving.
Stop - To stop the car.
Quit - To End the game.
""")
    else:
        print("Sorry, I don't understand that.")
