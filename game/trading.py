from quotas import *


def buy_all_you_can(item):
    most_possible = None
    all_costs = get_cost(item)
    for entry in all_costs:
        max_of_item = num_items(entry) / all_costs[entry]
        if most_possible == None:
            most_possible = max_of_item
        else:
            most_possible = min(max_of_item, most_possible)
    trade(item, most_possible)


def do_wood_trades():
    if not verify_quota(Items.Carrot_Seed):
        buy_all_you_can(Items.Carrot_Seed)
        return True
    if not verify_quota(Items.Water_Tank):
        buy_all_you_can(Items.Water_Tank)
        return True
    if not verify_quota(Items.Empty_Tank):
        trade(Items.Empty_Tank)
        return True
    return False


def do_carrot_trades():
    if not verify_quota(Items.Pumpkin_Seed):
        buy_all_you_can(Items.Pumpkin_Seed)
        return True
    if not verify_quota(Items.Sunflower_Seed):
        buy_all_you_can(Items.Sunflower_Seed)
        return True
    return False


def do_pumpkin_trades():
    if not verify_quota(Items.Fertilizer):
        buy_all_you_can(Items.Fertilizer)
        return True
    return False


def do_maze_trades():
    if not verify_quota(Items.Cactus_Seed):
        buy_all_you_can(Items.Cactus_Seed)
        return True
