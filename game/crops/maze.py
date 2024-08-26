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


CONST_LAYERS = 10


def solve_maze():
    cell_possible_directions = {}
    last_moved_dir = North
    destination = None
    for x in range(get_world_size()):
        for y in range(get_world_size()):
            cell_possible_directions[(x, y)] = {North, South, East, West}

    for i in range(CONST_LAYERS):
        kill_prev_cell = False
        cell_practical_directions = {}
        for cell in cell_possible_directions:
            new_set = set()
            for direction in cell_possible_directions[cell]:
                new_set.add(direction)
            cell_practical_directions[cell] = new_set
        while get_entity_type() == Entities.Hedge:
            if kill_prev_cell:
                cell_practical_directions[cur_pos()] = make_set_without(cell_practical_directions[cur_pos()],
                                                                        opposite(last_moved_dir))
                kill_prev_cell = False
            if len(cell_practical_directions[cur_pos()]) == 1:
                kill_prev_cell = True
            move_to = random_from_set(make_set_without(cell_practical_directions[cur_pos()], opposite(last_moved_dir)))
            if move_to == None:
                move_to = opposite(last_moved_dir)
                kill_prev_cell = True
            success = move(move_to)
            if not success:
                cell_possible_directions[cur_pos()] = make_set_without(cell_possible_directions[cur_pos()], move_to)
                cell_practical_directions[cur_pos()] = make_set_without(cell_practical_directions[cur_pos()], move_to)
            else:
                last_moved_dir = move_to
        if i != CONST_LAYERS - 1:
            quick_print("Fertilized:")
            quick_print(i)
            destination = measure()
            while get_entity_type() == Entities.Treasure:
                use_item(Items.Fertilizer)


def farm_maze():
    plant_maze()
    solve_maze()
    harvest()
