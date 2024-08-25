from bushes import *


def will_farm_trees():
    return will_farm_bushes()


def init_farm_trees():
    tree_traverse(plant_tree)


def plant_tree():
    harvest()
    try_water()
    plant(Entities.Tree)


def farm_tree():
    tree_traverse(check_tree)


def check_tree():
    if can_harvest():
        harvest()
        plant(Entities.Tree)
    try_water()


def tree_traverse(action):
    for x in range(0, get_world_size(), 2):
        for y in range(0, get_world_size(), 2):
            traverse(x, y)
            action()
