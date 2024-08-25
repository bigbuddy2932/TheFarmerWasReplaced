from ..farming import *


def will_farm_bushes():
    return not verify_quota(Items.Wood)


def plant_bush():
    harvest()
    plant(Entities.Bush)


def check_bush():
    if can_harvest():
        plant_bush()


def init_farm_bush():
    full_snake_path(plant_bush)


def farm_bush():
    full_snake_path(check_bush)
