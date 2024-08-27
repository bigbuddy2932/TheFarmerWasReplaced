from bushes import *
from ..collection_lib import *


def will_farm_maze():
    return num_items(Items.Fertilizer) > CONST_FERTILIZER_QUOTA / 2 and not verify_quota(Items.Gold)


def init_farm_maze():
    pass


def plant_maze():
    traverse(0, 0)
    plant_bush()
    while get_entity_type() == Entities.Bush and num_items(Items.Fertilizer) > 0:
        use_item(Items.Fertilizer)

# this is memory intensive, but its pretty fast!
def solve_maze():
    cell_possible_directions = {}  # Map<Point, Map<Cardinal, Set<Point>>
    need_to_check = set()
    exposed = []
    treasure_location = None
    for x in range(get_world_size()):
        for y in range(get_world_size()):
            need_to_check.add((x, y))
    while True:
        current_position = get_pos()
        if get_entity_type() == Entities.Treasure:
            treasure_location = current_position

        possible_movements_for_current_cell = check_movements()

        cardinal_locator_map = {}
        for cardinal in possible_movements_for_current_cell:
            check_cell = apply_direction(current_position, cardinal)
            if check_cell in need_to_check and check_cell not in exposed:
                exposed.append(check_cell)
            access_list = set()
            find_all_accessible_from(check_cell, opposite(cardinal), cell_possible_directions, access_list, exposed, need_to_check)
            cardinal_locator_map[cardinal] = access_list

        cell_possible_directions[current_position] = cardinal_locator_map

        need_to_check.remove(current_position)

        if len(need_to_check) > 0:
            next_cell = exposed.pop()
            navigate_to_cell(next_cell, cell_possible_directions, exposed, need_to_check)
        else:
            break
    refresh_all_accessible_from(cell_possible_directions, exposed, need_to_check)
    for i in range(299):
        navigate_to_cell(treasure_location, cell_possible_directions, exposed, need_to_check)
        treasure_location = measure()
        while get_entity_type() == Entities.Treasure and num_items(Items.Fertilizer):
            use_item(Items.Fertilizer)
    navigate_to_cell(treasure_location, cell_possible_directions, exposed, need_to_check)


def find_all_accessible_from(cell, direction, cell_possible_directions, output, exposed, need_to_check):
    output.add(cell)
    if cell in cell_possible_directions:
        for cardinal in cell_possible_directions[cell]:
            if cardinal != direction:
                find_all_accessible_from(apply_direction(cell, cardinal), opposite(cardinal), cell_possible_directions, output, exposed, need_to_check)


def refresh_all_accessible_from(cell_possible_directions, exposed, need_to_check):
    for cell in cell_possible_directions:
        for cardinal in cell_possible_directions[cell]:
            find_all_accessible_from(apply_direction(cell, cardinal), opposite(cardinal), cell_possible_directions, cell_possible_directions[cell][cardinal], exposed, need_to_check)


def navigate_to_cell(destination, cell_possible_directions, exposed, need_to_check):
    while get_pos() != destination:
        looped = True
        for cardinal in cell_possible_directions[get_pos()]:
            if destination in cell_possible_directions[get_pos()][cardinal]:
                move(cardinal)
                looped = False
                break
        if looped:
            refresh_all_accessible_from(cell_possible_directions, exposed, need_to_check)
            print("there is a navigation issue")


def check_movements():
    possible_movements = set()
    check_movement(North, possible_movements)
    check_movement(South, possible_movements)
    check_movement(East, possible_movements)
    check_movement(West, possible_movements)
    return possible_movements


def check_movement(cardinal, possible_movements):
    if move(cardinal):
        move(opposite(cardinal))
        possible_movements.add(cardinal)


def make_cardinals():
    return {North, South, East, West}


def farm_maze():
    plant_maze()
    solve_maze()
    harvest()
