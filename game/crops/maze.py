from bushes import *
from ..collection_lib import *


def will_farm_maze():
    return num_items(Items.Fertilizer) > CONST_FERTILIZER_QUOTA / 2 and not verify_quota(Items.Gold)


def init_farm_maze():
    pass


def plant_maze():
    traverse(0, 0)
    plant_bush()
    while get_entity_type() != Entities.Hedge and num_items(Items.Fertilizer) > 0:
        use_item(Items.Fertilizer)


def solve_maze():
    cell_is_dead = {}
    cell_possible_directions = {}
    last_moved_dir = North
    for x in range(get_world_size()):
        for y in range(get_world_size()):
            cell_is_dead[(x, y)] = False
            cell_possible_directions[(x, y)] = {North, South, East, West}

    while get_entity_type() == Entities.Hedge:
        current_cell_directions = cell_possible_directions[cur_pos()]
        move_to = random_from_set(make_set_without(current_cell_directions, opposite(last_moved_dir)))
        if move_to == None:
            move_to = opposite(last_moved_dir)
            quick_print(move_to)
        success = move(move_to)
        if not success:
            cell_possible_directions[cur_pos()] = make_set_without(current_cell_directions, move_to)
        else:
            last_moved_dir = move_to



def farm_maze():
    plant_maze()
    solve_maze()
    harvest()
