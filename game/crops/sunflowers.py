from ..farming import *


def will_farm_sunflowers():
    return num_items(Items.Sunflower_Seed) > 0 and not verify_quota(Items.Power)


def init_farm_sunflowers():
    pass


def init_farm_sunflowers_tile():
    check_till()
    try_water()
    plant(Entities.Sunflower)
    return measure()


def farm_sunflowers():
    petal_counts = {}

    for pedals in range(7, 16):
        petal_counts[pedals] = set()

    for x in range(get_world_size()):
        for y in range(get_world_size()):
            traverse(x, y)
            petal_counts[init_farm_sunflowers_tile()].add((x, y))

    for pedals in range(15, 6, -1):
        while len(petal_counts[pedals]) > 0:
            to_remove = []
            for point in petal_counts[pedals]:
                traverse(point[0], point[1])
                if can_harvest():
                    harvest()
                    to_remove.append(point)
            for point in to_remove:
                petal_counts[pedals].remove(point)


