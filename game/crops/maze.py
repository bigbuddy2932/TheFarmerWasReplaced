from bushes import *


def will_farm_maze():
    return num_items(Items.Fertilizer) > CONST_FERTILIZER_QUOTA / 2 and not verify_quota(Items.Gold)


def init_farm_maze():
    pass


def plant_maze():
    traverse(0, 0)
    plant_bush()
    while get_entity_type() != Entities.Hedge and num_items(Items.Fertilizer) > 0:
        use_item(Items.Fertilizer)


def farm_maze():
    plant_maze()
    i = 0
    while get_entity_type() == Entities.Hedge and i < 1000:
        dir = random() * 4
        if dir >= 3:
            if not move(North):
                move(East)
        elif dir >= 2:
            if not move(South):
                move(West)
        elif dir >= 1:
            if not move(East):
                move(South)
        else:
            if not move(West):
                move(North)
        i += 1
        if i % 100 == 99:
            quick_print(i)
    harvest()
