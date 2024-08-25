from ..farming import *


def will_farm_hay():
    return not verify_quota(Items.Hay)


def init_farm_hay():
    clear()


def farm_hay():
    full_snake_path(harvest)
