from ..farming import *


def will_farm_dinosaurs():
    return not verify_quota(Items.Bones) and num_items(Items.Egg) > get_world_size() * get_world_size()


def init_farm_dinosaurs():
    init_farm_dinosaurs_tile(harvest)


def init_farm_dinosaurs_tile():
    check_till()
    try_water()
    plant(Entities.Dinosaur)



def farm_dinosaur():
    full_snake_path(harvest)