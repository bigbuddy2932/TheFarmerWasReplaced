from __builtins__ import *

CONST_HAY_QUOTA = get_world_size() * get_world_size() * 64
CONST_WOOD_QUOTA = get_world_size() * get_world_size() * 64
CONST_WATER_TANK_QUOTA = 100
CONST_EMPTY_TANK_QUOTA = 5
CONST_CARROT_SEED_QUOTA = get_world_size() * get_world_size() * 8
CONST_CARROT_QUOTA = get_world_size() * get_world_size() * 64
CONST_PUMPKIN_SEED_QUOTA = get_world_size() * get_world_size() * 8
CONST_PUMPKIN_QUOTA = get_world_size() * get_world_size() * 64
CONST_SUNFLOWER_SEED_QUOTA = get_world_size() * get_world_size() * 8
CONST_FERTILIZER_QUOTA = get_world_size() * get_world_size() * 8
CONST_POWER_QUOTA = get_world_size() * get_world_size() * 64
CONST_GOLD_QUOTA = get_world_size() * get_world_size() * 64
# Special quota for watering
CONST_WATER_LEVEL_QUOTA = 0.75

quotas = {Items.Hay: CONST_HAY_QUOTA, Items.Wood: CONST_WOOD_QUOTA, Items.Water_Tank: CONST_WATER_TANK_QUOTA,
          Items.Empty_Tank: CONST_EMPTY_TANK_QUOTA, Items.Carrot_Seed: CONST_CARROT_SEED_QUOTA,
          Items.Carrot: CONST_CARROT_QUOTA, Items.Pumpkin_Seed: CONST_PUMPKIN_SEED_QUOTA,
          Items.Pumpkin: CONST_PUMPKIN_QUOTA, Items.Sunflower_Seed: CONST_SUNFLOWER_SEED_QUOTA,
          Items.Fertilizer: CONST_FERTILIZER_QUOTA, Items.Power: CONST_POWER_QUOTA, Items.Gold: CONST_GOLD_QUOTA}


def verify_quota(item_to_verify):
    if item_to_verify in quotas:
        return num_items(item_to_verify) >= quotas[item_to_verify]
    return True
