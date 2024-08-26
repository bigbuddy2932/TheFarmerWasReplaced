from bushes import *


def init_farm_crude_maze():
    pass


def plant_crude_maze():
    traverse(0, 0)
    harvest()
    plant_bush()
    while get_entity_type() != Entities.Hedge and num_items(Items.Fertilizer) > 0:
        use_item(Items.Fertilizer)


def farm_crude_maze():
    plant_crude_maze()
    last_moved = South
    i = 0
    while get_entity_type() == Entities.Hedge and i < 1000:
        will_move = last_moved
        did_move = False
        failed_moved = 0
        while not did_move and failed_moved < 8:
            will_move = last_moved
            while will_move == last_moved:
                direction = random() * 4
                if direction >= 3:
                    will_move = North
                elif direction >= 2:
                    will_move = South
                elif direction >= 1:
                    will_move = East
                else:
                    will_move = West
            did_move = move(will_move)
            failed_moved += 1
        last_moved = opposite(will_move)
        i += 1
    harvest()
