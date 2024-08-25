from farming import *


def init_farm_pumpkin():
    full_snake_path(init_farm_pumpkin_tile)


def init_farm_pumpkin_tile():
    harvest()
    check_till()
    try_water()
    plant(Entities.Pumpkin)


def farm_pumpkin():
    all_ready = False

    while not all_ready:
        if num_items(Items.Pumpkin_Seed) == 0:
            full_snake_path(harvest)
            break
        all_ready = True
        initx = 0
        inity = 0
        width = get_world_size()-1
        height = get_world_size()-1

        traverse(initx, inity)
        right_bound = initx + width
        top_bound = inity + height
        for x in range(initx, right_bound + 1):
            if get_pos_y() == top_bound:
                while get_pos_y() != inity:
                    if not check_pumpkin_tile():
                        all_ready = False
                    move(South)
            else:
                while get_pos_y() != top_bound:
                    if not check_pumpkin_tile():
                        all_ready = False
                    move(North)
            if x != right_bound:
                if not check_pumpkin_tile():
                    all_ready = False
                move(East)
        if not check_pumpkin_tile():
            all_ready = False
    harvest()


def check_pumpkin_tile():
    if get_entity_type() != Entities.Pumpkin:
        init_farm_pumpkin_tile()
        return False
    return can_harvest()
