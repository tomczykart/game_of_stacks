"""This is first prototype of a game of stack"""

from collections import namedtuple
import json


# Lets keep stack in a file
def save_stack(stack):
    with open("data.json", "w") as f:
        json.dump(stack, f)


# Read stack data from file
def read_stacks():
    with open("data.json", "r") as f:
        return json.load(f)


# Each stack will be a dict with name and tuple with digits as 6 walls
def choose_stack(name, walls):
    if isinstance(name, str) and isinstance(walls, tuple) and len(walls) == 6:
        return {name: walls}


if __name__ == "__main__":
    print("Hello, World!")

    # read data from file
    stacks = read_stacks()

    # stack counter
    counter = stacks["counter"]
    print(f"Thre are {counter} stacks in the tower")

    # add new element
    stack1 = choose_stack("stack_001", (9, 3, 3, 0, 5, 4))
    stack2 = choose_stack("stack_002", (7, 7, 7, 0, 5, 4))
    stacks.update(stack1)
    stacks.update(stack2)

    # write to file whole dict
    save_stack(stacks)

    # verify
    stacks = read_stacks()
    print(stacks)
