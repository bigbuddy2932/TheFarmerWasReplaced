from farming import *


def plant_bush():
    plant(Entities.Bush)


def check_bush():
    if can_harvest():
        harvest()
        plant_bush()


def init_farm_bush():
    full_snake_path(plant_bush)


def farm_bush():
    full_snake_path(check_bush)
