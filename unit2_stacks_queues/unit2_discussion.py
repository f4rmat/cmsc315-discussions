"""
===========================================================
UNIT 2 DISCUSSION: STACKS AND QUEUES (PYTHON)
===========================================================

OVERVIEW:
This assignment introduces two fundamental data structures:
the Stack (LIFO) and the Queue (FIFO).

You will complete, modify, and extend the starter code while
explaining key concepts through comments and improved output.
"""

from collections import deque


class Stack:
    def __init__(self):
        # A Python list is used to store stack values.
        self.items = []

    def push(self, value):
        # Appending to the end of the list supports LIFO behavior
        # (the last item added will be the first one removed).
        self.items.append(value)

    def pop(self):
        # Removes and returns the most recently added value.
        # Returning a string message prevents a runtime crash if the stack is empty.
        if self.is_empty():
            return "Error: Stack is empty"
        return self.items.pop()

    def peek(self):
        # Returns the top value without removing it.
        if self.is_empty():
            return "Error: Stack is empty"
        return self.items[-1]

    def is_empty(self):
        return len(self.items) == 0


class Queue:
    def __init__(self):
        # collections.deque is used for efficient O(1) additions and removals.
        self.items = deque()

    def enqueue(self, value):
        # Appending to the right side supports FIFO behavior
        # (items will be processed in the exact order they arrive).
        self.items.append(value)

    def dequeue(self):
        # Removes and returns the value from the front of the queue.
        # Returning a string message prevents a runtime crash if the queue is empty.
        if self.is_empty():
            return "Error: Queue is empty"
        return self.items.popleft()

    def front(self):
        # Returns the front value without removing it.
        if self.is_empty():
            return "Error: Queue is empty"
        return self.items[0]

    def is_empty(self):
        return len(self.items) == 0


def main():
    print("=== UNIT 2: STACKS AND QUEUES ===")

    # ===============================
    # STACK DEMO
    # ===============================
    print("\n=== STACK DEMO ===")
    print("Scenario: Undoing Home Assistant config edits")

    undo_stack = Stack()
    undo_stack.push("Edit 1: Added light entity")
    undo_stack.push("Edit 2: Changed timezone")
    undo_stack.push("Edit 3: Added MQTT broker")
    undo_stack.push("Edit 4: Updated dashboard theme")

    print(f"Undoing latest action: {undo_stack.pop()}")
    print(f"Undoing next action: {undo_stack.pop()}")
    print(f"Peeking at next to undo: {undo_stack.peek()}")

    print("\n-- Edge Cases (Stack) --")
    empty_stack = Stack()
    print(f"Popping from empty stack: {empty_stack.pop()}")
    print(f"Peeking at empty stack: {empty_stack.peek()}")

    single_stack = Stack()
    single_stack.push("Edit 5: Fixed YAML syntax")
    single_stack.pop()
    print(f"Is single-item stack empty after removal? {single_stack.is_empty()}")


    # ===============================
    # QUEUE DEMO
    # ===============================
    print("\n=== QUEUE DEMO ===")
    print("Scenario: Processing MQTT sensor data messages")

    mqtt_queue = Queue()
    mqtt_queue.enqueue("Message 1: Front Door Opened")
    mqtt_queue.enqueue("Message 2: Living Room Motion")
    mqtt_queue.enqueue("Message 3: Temp 72F")
    mqtt_queue.enqueue("Message 4: Humidity 45%")

    print(f"Processing first message: {mqtt_queue.dequeue()}")
    print(f"Processing next message: {mqtt_queue.dequeue()}")
    print(f"Next in line (front): {mqtt_queue.front()}")

    print("\n-- Edge Cases (Queue) --")
    empty_queue = Queue()
    print(f"Dequeuing from empty queue: {empty_queue.dequeue()}")
    print(f"Viewing front of empty queue: {empty_queue.front()}")

    single_queue = Queue()
    single_queue.enqueue("Message 5: Battery low")
    single_queue.dequeue()
    print(f"Is single-item queue empty after removal? {single_queue.is_empty()}")


if __name__ == "__main__":
    main()
