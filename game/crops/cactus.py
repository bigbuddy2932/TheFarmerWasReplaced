from ..farming import *


def will_farm_cactus():
    return not verify_quota(Items.Cactus) and num_items(Items.Cactus_Seed) > get_world_size() * get_world_size()


def init_farm_cactus():
    pass


def plant_cactus():
    harvest()
    check_till()
    plant(Entities.Cactus)


def try_swap_in_direction(cardinal):
    if measure() > measure(cardinal):
        swap(cardinal)
        return False
    return True


def sort_direction(traverse_axis, compare_cardinal):
    for set_axis in range(get_world_size()):
        traverse_axis(set_axis)
        for compare_axis_cap in range(get_world_size() - 1, -1, -1):
            traverse_axis(set_axis)
            is_sorted = True
            for compare_axis in range(compare_axis_cap):
                if not try_swap_in_direction(compare_cardinal):
                    is_sorted = False
                move(compare_cardinal)
            if is_sorted:
                break


def farm_cactus():
    full_snake_path(plant_cactus)
    traverse(0, 0)
    sort_direction(traverse_x, North)
    sort_direction(traverse_y, East)
    harvest()
