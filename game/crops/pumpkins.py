from ..farming import *


def will_farm_pumpkins():
    return num_items(Items.Pumpkin_Seed) > CONST_PUMPKIN_SEED_QUOTA / 2 and not verify_quota(Items.Pumpkin)


def init_farm_pumpkin():
    full_snake_path(init_farm_pumpkin_tile)


def init_farm_pumpkin_tile():
    harvest()
    check_till()
    try_water()
    plant(Entities.Pumpkin)


def farm_pumpkin():
    cells_to_check = {}
    for x in range(get_world_size()):
        for y in range(get_world_size()):
            cells_to_check[(x, y)] = None
    while len(cells_to_check) > 0:
        to_remove = []
        for cell in cells_to_check:
            traverse(cell[0], cell[1])
            if check_pumpkin_tile():
                to_remove.append(cell)
        for cell in to_remove:
            cells_to_check.pop(cell)
    harvest()


def check_pumpkin_tile():
    if get_entity_type() != Entities.Pumpkin:
        init_farm_pumpkin_tile()
        return False
    return can_harvest()
