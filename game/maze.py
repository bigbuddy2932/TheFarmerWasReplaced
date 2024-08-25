from bushes import *


def init_farm_maze():
    noop = 0


def plant_maze():
    traverse(0, 0)
    harvest()
    plant_bush()
    while get_entity_type() != Entities.Hedge and num_items(Items.Fertilizer) > 0:
        use_item(Items.Fertilizer)


def farm_maze():
    plant_maze()
    while get_entity_type() == Entities.Hedge:
        dir = random() * 4
        if dir >= 3:
            move(North)
        elif dir >= 2:
            move(South)
        elif dir >= 1:
            move(East)
        else:
            move(West)
    harvest()
