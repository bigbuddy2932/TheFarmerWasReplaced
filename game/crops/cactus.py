from ..farming import *


def will_farm_cactus():
    return not verify_quota(Items.Cactus)


def init_farm_cactus():
    full_snake_path(harvest_and_till)


def harvest_and_till():
    harvest()
    check_till()


def plant_cactus():
    harvest()
    plant(Entities.Cactus)


def farm_cactus():
    full_snake_path(plant_cactus)
