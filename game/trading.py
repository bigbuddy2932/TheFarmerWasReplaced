from quotas import *


def do_wood_trades():
    if not verify_quota(Items.Carrot_Seed):
        trade(Items.Carrot_Seed, CONST_CARROT_SEED_QUOTA - num_items(Items.Carrot_Seed) + 1)
        return True
    if not verify_quota(Items.Water_Tank):
        trade(Items.Empty_Tank, CONST_WATER_TANK_QUOTA - num_items(Items.Water_Tank) + 1)
        return True
    if not verify_quota(Items.Empty_Tank):
        trade(Items.Empty_Tank, CONST_EMPTY_TANK_QUOTA)
        return True
    return False


def do_carrot_trades():
    if not verify_quota(Items.Pumpkin_Seed):
        trade(Items.Pumpkin_Seed, CONST_PUMPKIN_SEED_QUOTA - num_items(Items.Pumpkin_Seed) + 1)
        return True
    if not verify_quota(Items.Sunflower_Seed):
        trade(Items.Sunflower_Seed, CONST_SUNFLOWER_SEED_QUOTA - num_items(Items.Sunflower_Seed) + 1)
        return True
    return False


def do_pumpkin_trades():
    if not verify_quota(Items.Fertilizer):
        trade(Items.Fertilizer, CONST_FERTILIZER_QUOTA - num_items(Items.Fertilizer) + 1)
        return True
    return False
