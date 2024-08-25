from farming import *


def will_farm_sunflowers():
    return num_items(Items.Sunflower_Seed) > 0 and not verify_quota(Items.Power)


def init_farm_sunflowers():
    full_snake_path(init_farm_sunflowers_tile)


def init_farm_sunflowers_tile():
    till()
    try_water()
    plant(Entities.Sunflower)


def farm_sunflowers():
    full_snake_path(harvest)
