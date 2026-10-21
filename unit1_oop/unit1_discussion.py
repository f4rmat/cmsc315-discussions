"""
===========================================================
Unit 1 DISCUSSION: Python OOP, Namespaces, and Copying
===========================================================

INSTRUCTIONS:
In this assignment, you will build and explore object-oriented programming (OOP) concepts in Python.
You are provided with starter code containing TODO sections. Your task is to complete, modify, and
analyze the code to demonstrate understanding of inheritance, namespaces, and object copying.
"""


from copy import copy, deepcopy


# TODO 1:
# Create a parent class.
#
# Requirements:
# - Include at least one class variable.
# - Include at least two instance variables.
# - Include a constructor (__init__).
# - Include a method that returns or displays information about the object.
#
# Replace the pass statement with your implementation.

class Device:
    """A generic smart-home device."""
    hub_name = "HomeHub"          # class variable, shared by all devices

    def __init__(self, name, room):
        self.name = name            # instance variable 1
        self.room = room            # instance variable 2
        self._is_on = False

    def describe(self):
        state = "ON" if self._is_on else "OFF"
        return f"[{self.hub_name}] {self.name} in {self.room} is {state}"

# TODO 2:
# Create a child class that inherits from the parent class.
#
# Requirements:
# - Use inheritance.
# - Add at least one new class variable.
# - Add at least two new instance variables.
# - Add at least one new method.
# - Override a method from the parent class.
#
# Replace the pass statement with your implementation.

class SmartLock(Device):
    """A smart lock: a device that also locks and checks a code."""
    max_failed_attempts = 3

    def __init__(self, name, room, code):
        super().__init__(name, room) # the two values the parent needs
        self._code = str(code)
        self.is_locked = True
        self.failed_attempts = 0
        self.access_log = []

    def unlock(self, code):
        if self.failed_attempts >= self.max_failed_attempts: # too many tries already
            self.access_log.append("blocked")
            return False
        if str(code) != self._code: # wrong code
            self.failed_attempts += 1
            self.access_log.append("failed attempt")
            return False
        self.is_locked = False
        self.failed_attempts = 0
        self.access_log.append("unlocked")
        return True

    def describe(self):
        base = super().describe()                     # the parent's text
        lock_state = "LOCKED" if self.is_locked else "UNLOCKED"
        return f"{base}, {lock_state}"



# TODO 3:
# Create a function that demonstrates class namespaces and instance namespaces.
#
# Your function should:
# - Create at least two objects of the child class.
# - Access a class variable through the class itself.
# - Access the same class variable through an object.
# - Add a new attribute to only one object after it is created.
# - Display each object's namespace using __dict__.
# - Display information about the class namespace.

def demonstrate_namespaces():
    print("\n=== Namespace Demonstration ===")
    front = SmartLock("Front Door", "Entry", 1234)
    back = SmartLock("Back Door", "Kitchen", 5678)
    print("Through the class :", SmartLock.max_failed_attempts)
    print("Through an object :", front.max_failed_attempts)
    front.battery_level = 87 # only front gets this
    print("front has it?", hasattr(front, "battery_level"))
    print("back has it? ", hasattr(back, "battery_level"))
    print("front namespace:", front.__dict__)
    print("back namespace: ", back.__dict__)
    print("class namespace:", [k for k in SmartLock.__dict__ if not k.startswith("__")])

# TODO 4:
# Create a function that demonstrates shallow copying and deep copying.
#
# Requirements:
# - Create an object that contains nested mutable data.
# - Create a shallow copy.
# - Create a deep copy.
# - Modify the original object's nested data.
# - Display the original object, shallow copy, and deep copy.
# - Use comments to explain the difference between shallow and deep copying.

def demonstrate_copying():
    print("\n=== Copy Demonstration ===")
    original = SmartLock("Garage", "Garage", 2468)
    original.access_log.append("installed")
    shallow = copy(original)
    deep = deepcopy(original)
    original.access_log.append("unlocked by owner")
    # Shallow copy changes because it only copy the reference of the item
    # Deep copy does not change because it copies the actual item with new reference
    print("original log:", original.access_log)
    print("shallow log: ", shallow.access_log)
    print("deep log:    ", deep.access_log)


# TODO 5:
# Complete the main function.
#
# Requirements:
# - Create at least one object from the parent class.
# - Create at least one object from the child class.
# - Demonstrate inheritance by calling methods.
# - Call your namespace demonstration function.
# - Call your copy demonstration function.

def main():
    print("=== Unit 1 OOP Assignment ===")
    lamp = Device("Desk Lamp", "Office")
    print(lamp.describe())
    door = SmartLock("Front Door", "Entry", 1234)
    print(door.describe())
    print("wrong code:", door.unlock(1111))
    print("right code:", door.unlock(1234))
    print(door.describe())
    demonstrate_namespaces()
    demonstrate_copying()


if __name__ == "__main__":
    main()
