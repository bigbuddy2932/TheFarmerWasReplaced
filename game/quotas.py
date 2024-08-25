from __builtins__ import *

CONST_HAY_QUOTA = 10000
CONST_WOOD_QUOTA = get_world_size() * get_world_size() * 64
CONST_WATER_TANK_QUOTA = 100
CONST_EMPTY_TANK_QUOTA = 5
CONST_CARROT_SEED_QUOTA = get_world_size() * get_world_size() * 4
CONST_CARROT_QUOTA = get_world_size() * get_world_size() * 64
CONST_PUMPKIN_SEED_QUOTA = get_world_size() * get_world_size() * 8
CONST_PUMPKIN_QUOTA = 10000
CONST_SUNFLOWER_SEED_QUOTA = get_world_size() * get_world_size() * 8
CONST_FERTILIZER_QUOTA = 200
CONST_SUNFLOWER_QUOTA = 10000
CONST_WATER_LEVEL_QUOTA = 0.75

def verify_quota(item_to_verify):
    if item_to_verify == Items.Hay:
        return num_items(item_to_verify) >= CONST_HAY_QUOTA
    elif item_to_verify == Items.Wood:
        return num_items(item_to_verify) >= CONST_WOOD_QUOTA
    elif item_to_verify == Items.Water_Tank:
        return num_items(item_to_verify) >= CONST_WATER_TANK_QUOTA
    elif item_to_verify == Items.Empty_Tank:
        return num_items(item_to_verify) >= CONST_EMPTY_TANK_QUOTA
    elif item_to_verify == Items.Carrot_Seed:
        return num_items(item_to_verify) >= CONST_CARROT_SEED_QUOTA
    elif item_to_verify == Items.Carrot:
        return num_items(item_to_verify) >= CONST_CARROT_QUOTA
    elif item_to_verify == Items.Pumpkin_Seed:
        return num_items(item_to_verify) >= CONST_PUMPKIN_SEED_QUOTA
    elif item_to_verify == Items.Pumpkin:
        return num_items(item_to_verify) >= CONST_PUMPKIN_QUOTA
    elif item_to_verify == Items.Sunflower_Seed:
        return num_items(item_to_verify) >= CONST_SUNFLOWER_SEED_QUOTA
    elif item_to_verify == Items.Fertilizer:
        return num_items(item_to_verify) >= CONST_FERTILIZER_QUOTA
    return True
