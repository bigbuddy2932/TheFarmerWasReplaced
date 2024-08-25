from game.__builtins__ import *


def make_set_without(set_in, exclude):
    new_set = set()
    for i in set_in:
        if i != exclude:
            new_set.add(i)
    return new_set


def random_from_set(choose_from):
    if len(choose_from) == 0:
        return None
    temp = []
    for i in choose_from:
        temp.append(i)
    return temp[random() * len(temp)]
