from movement import *
from quotas import *


def try_water():
    if num_items(Items.Water_Tank) > 0 and get_water() < CONST_WATER_LEVEL_QUOTA:
        use_item(Items.Water_Tank)


def till_all():
    full_snake_path(check_till)


def check_till():
    if get_ground_type() != Grounds.Soil:
        till()


def check_untill():
    if get_ground_type() != Grounds.Turf:
        till()
