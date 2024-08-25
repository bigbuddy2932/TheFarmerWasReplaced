from crop_imports import *

will_farm_methods = {Entities.Grass: will_farm_hay, Entities.Bush: will_farm_bushes,
                     Entities.Carrots: will_farm_carrots, Entities.Pumpkin: will_farm_pumpkins,
                     Entities.Sunflower: will_farm_sunflowers, Entities.Treasure: will_farm_maze,
                     Entities.Tree: will_farm_trees}


def will_farm_entity(entity_to_farm):
    if entity_to_farm in will_farm_methods:
        return will_farm_methods[entity_to_farm]()
    return False


init_methods = {Entities.Grass: init_farm_hay, Entities.Bush: init_farm_bush, Entities.Carrots: init_farm_carrot,
                Entities.Pumpkin: init_farm_pumpkin, Entities.Sunflower: init_farm_sunflowers,
                Entities.Treasure: init_farm_maze, Entities.Tree: init_farm_trees}


def init_entity(entity_to_farm):
    init_methods[entity_to_farm]()


farm_methods = {Entities.Grass: farm_hay, Entities.Bush: farm_bush, Entities.Carrots: farm_carrot,
                Entities.Pumpkin: farm_pumpkin, Entities.Sunflower: farm_sunflowers, Entities.Treasure: farm_maze,
                Entities.Tree: farm_tree}


def farm_entity(entity_to_farm):
    farm_methods[entity_to_farm]()


def try_farm_entity(entity_to_farm):
    if will_farm_entity(entity_to_farm):
        init_entity(entity_to_farm)
        while will_farm_entity(entity_to_farm):
            farm_entity(entity_to_farm)
        return True
    return False


TO_VERIFY = [Items.Hay, Items.Wood, Items.Water_Tank, Items.Empty_Tank, Items.Carrot_Seed, Items.Carrot, Items.Pumpkin,
             Items.Pumpkin_Seed, Items.Power, Items.Gold]


def verify_all_quotas():
    for item in TO_VERIFY:
        if not verify_quota(item):
            quick_print("Quota not hit for:")
            quick_print(item)
            quick_print("Has:")
            quick_print(num_items(item))
            quick_print("Needs:")
            quick_print(quotas[item])
            return False
    print("QUOTAS MET")
    return True


def force_farm_entity(entity_to_farm):
    if not verify_all_quotas():
        print("DEATH LOOP")
        return
    init_entity(entity_to_farm)
    while verify_all_quotas():
        farm_entity(entity_to_farm)
