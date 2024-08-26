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
CONST_CACTUS_SEED_QUOTA = get_world_size() * get_world_size() * 8
CONST_CACTUS_QUOTA = get_world_size() * get_world_size() * 64
# Special quota for watering
CONST_WATER_LEVEL_QUOTA = 0.75

default_quotas = {Items.Hay: CONST_HAY_QUOTA, Items.Wood: CONST_WOOD_QUOTA, Items.Water_Tank: CONST_WATER_TANK_QUOTA,
                  Items.Empty_Tank: CONST_EMPTY_TANK_QUOTA, Items.Carrot_Seed: CONST_CARROT_SEED_QUOTA,
                  Items.Carrot: CONST_CARROT_QUOTA, Items.Pumpkin_Seed: CONST_PUMPKIN_SEED_QUOTA,
                  Items.Pumpkin: CONST_PUMPKIN_QUOTA, Items.Sunflower_Seed: CONST_SUNFLOWER_SEED_QUOTA,
                  Items.Fertilizer: CONST_FERTILIZER_QUOTA, Items.Power: CONST_POWER_QUOTA,
                  Items.Gold: CONST_GOLD_QUOTA, Items.Cactus_Seed: CONST_CACTUS_SEED_QUOTA,
                  Items.Cactus: CONST_CACTUS_QUOTA}

quotas = {}

auto_unlock_candidates = [Unlocks.Expand, Unlocks.Speed, Unlocks.Carrots, Unlocks.Benchmark, Unlocks.Debug_2,
                          Unlocks.Sunflowers, Unlocks.Dinosaurs, Unlocks.Auto_Unlock, Unlocks.Leaderboard]


def refresh_quotas():
    for item in default_quotas:
        if item not in quotas:
            quotas[item] = default_quotas[item]
    for unlock_element in auto_unlock_candidates:
        cost = get_cost(unlock_element)
        if cost != None:
            for item in cost:
                if item in quotas:
                    quotas[item] = max(quotas[item], cost[item])


refresh_quotas()


def verify_quota(item_to_verify):
    if item_to_verify in quotas:
        return num_items(item_to_verify) >= quotas[item_to_verify]
    return True
