"""This is first prototype of a game of stack"""

from collections import namedtuple
import json


# Each stack will be a dict with name and tuple with digits as 6 walls
def choose_stack(name, walls):
    if isinstance(name, str) and isinstance(walls, tuple) and len(walls) == 6:
        return {name: walls}


# Lets keep stack in a file
def save_stack(stack):
    with open("data.json", "w") as f:
        json.dump(stack, f)


if __name__ == "__main__":
    print("Hello, World!")
    stack1 = choose_stack("stack1", (1, 3, 3, 4, 5, 9))
    save_stack(stack1)
