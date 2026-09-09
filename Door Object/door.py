class Door:
    def __init__(self, is_open, is_locked, door_color, num_open):
        self.is_open = is_open
        self.is_locked = is_locked
        self.door_color = door_color
        self.num_open = num_open

    def open(self):
        if self.is_open:
            print("The door is already open")
        elif self.is_locked:
            print("The door is locked")
        else:
            self.is_open = True
            self.num_open += 1
            print("The door is now open")

    def close(self):
        if not self.is_open:
            print ("The door is already closed")
        else:
            self.is_open = False
            print("The door is now closed")

    def lock(self):
        if self.is_locked:
            print("The door is already locked")
        elif self.is_open:
            print("The door is open and cannot be locked")
        else:
            self.is_locked = True
            print("The door is now locked")

    def unlock(self):
        if not self.is_locked:
            print("The door is already unlocked")
        else:
            self.is_locked = False
            print("The door is now unlocked")

    def color(self):
        print("Type no to not change color")
        user_input = input("What should the door color be changed to:").strip().lower()
        if self.door_color == user_input:
            print("Door is already that color")
        elif user_input == "no":
            print(f"The door is still {self.door_color}")
        else:
            self.door_color = user_input
            print(f"The door is now {self.door_color}")

    def times_open(self):
        print(f"You opened the door {self.num_open} times")

    def knock(self):
        if self.is_open:
            print("Door is open and cannot be knocked on")
        else:
            print("Knock knock")


