from farming import *


def init_farm_sunflowers():
    full_snake_path(init_farm_sunflowers_tile)

def init_farm_sunflowers_tile():
    till()
    try_water()
    plant(Entities.Sunflower)

def farm_sunflowers():
    full_snake_path(harvest)
