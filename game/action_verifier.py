from crop_imports import *


def will_farm_entity(entity_to_farm):
    if entity_to_farm == Entities.Grass:
        return not verify_quota(Items.Hay)
    elif entity_to_farm == Entities.Bush:
        return not verify_quota(Items.Wood)
    elif entity_to_farm == Entities.Carrots:
        return num_items(Items.Carrot_Seed) > 0 and not verify_quota(Items.Carrot)
    elif entity_to_farm == Entities.Pumpkin:
        return num_items(Items.Pumpkin_Seed) > CONST_PUMPKIN_SEED_QUOTA / 2 and not verify_quota(Items.Pumpkin)
    elif entity_to_farm == Entities.Sunflower:
        return num_items(Items.Sunflower_Seed) > 0 and not verify_quota(Items.Power)
    elif entity_to_farm == Items.Gold:
        return not verify_quota(Items.Gold)
    return False


def init_entity(entity_to_farm):
    if entity_to_farm == Entities.Grass:
        init_farm_hay()
    elif entity_to_farm == Entities.Bush:
        init_farm_bush()
    elif entity_to_farm == Entities.Carrots:
        init_farm_carrot()
    elif entity_to_farm == Entities.Pumpkin:
        init_farm_pumpkin()
    elif entity_to_farm == Entities.Sunflower:
        init_farm_sunflowers()
    elif entity_to_farm == Items.Gold:
        init_farm_maze()


def farm_entity(entity_to_farm):
    if entity_to_farm == Entities.Grass:
        farm_hay()
    elif entity_to_farm == Entities.Bush:
        farm_bush()
    elif entity_to_farm == Entities.Carrots:
        farm_carrot()
    elif entity_to_farm == Entities.Pumpkin:
        farm_pumpkin()
    elif entity_to_farm == Entities.Sunflower:
        farm_sunflowers()
    elif entity_to_farm == Items.Gold:
        farm_maze()


def try_farm_entity(entity_to_farm):
    if will_farm_entity(entity_to_farm):
        init_entity(entity_to_farm)
        while will_farm_entity(entity_to_farm):
            farm_entity(entity_to_farm)
        return True
    return False


TO_VERIFY = [Items.Hay, Items.Wood, Items.Water_Tank, Items.Empty_Tank, Items.Carrot_Seed, Items.Carrot, Items.Pumpkin,
             Items.Pumpkin_Seed, Items.Gold]


def verify_all_quotas():
    for item in TO_VERIFY:
        if not verify_quota(item):
            return False
    print("QUOTAS HIT")
    return True


def force_farm_entity(entity_to_farm):
    if not verify_all_quotas():
        print("DEATH LOOP")
        return
    init_entity(entity_to_farm)
    while verify_all_quotas():
        farm_entity(entity_to_farm)
