from door import Door

door = Door(False, True, "black", 0)
door2 = Door(True, False, "White", 0)

used_door = """Which door do you want to use:
| DOOR | DOOR2 |"""

message = """Enter a command:
| OPEN | CLOSE | LOCK | UNLOCK | COLOR | TIMES_OPEN | KNOCK |\n"""

commands = [
    "open",
    "close",
    "lock",
    "unlock",
    "color",
    "times_open",
    "knock",
]

actions = [
    door.open,
    door.close,
    door.lock,
    door.unlock,
    door.color,
    door.times_open,
    door.knock,
]

actions2 = [
    door2.open,
    door2.close,
    door2.lock,
    door2.unlock,
    door2.color,
    door2.times_open,
    door2.knock,
]

while True:
    door_num = input(used_door).strip().lower()
    print("Type exit to end the program")
    user_input = input(message).strip().lower()
    for command, action, action2 in zip(commands, actions, actions2):
        if user_input == command:
            if door_num == "door":
                action()
                break
            elif door_num == "door2":
                action2()
                break
    else:
        if user_input == "exit":
            break
        print("Invalid command")