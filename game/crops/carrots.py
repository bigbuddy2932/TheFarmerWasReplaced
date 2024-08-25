from ..farming import *


def will_farm_carrots():
    return num_items(Items.Carrot_Seed) > 0 and not verify_quota(Items.Carrot)


def plant_carrots():
    if num_items(Items.Carrot_Seed) > 0:
        check_till()
        try_water()
        plant(Entities.Carrots)


def check_carrots():
    if can_harvest():
        harvest()
        plant_carrots()


def init_farm_carrot():
    full_snake_path(init_farm_carrot_tile)


def init_farm_carrot_tile():
    harvest()
    plant_carrots()


def farm_carrot():
    full_snake_path(check_carrots)
