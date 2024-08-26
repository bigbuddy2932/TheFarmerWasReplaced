from quotas import *


def do_trade(item):
    buy_all_you_can(item)


def buy(item):
    trade(item)


def buy_ten(item):
    trade(item, 10)


def buy_all_you_can(item):
    most_possible = None
    all_costs = get_cost(item)
    for entry in all_costs:
        max_of_item = num_items(entry) / all_costs[entry]
        if most_possible == None:
            most_possible = max_of_item
        else:
            most_possible = min(max_of_item, most_possible)
    if (most_possible == None):
        most_possible = 1
    trade(item, most_possible)


def do_wood_trades():
    if not verify_quota(Items.Carrot_Seed):
        do_trade(Items.Carrot_Seed)
        return True
    if not verify_quota(Items.Water_Tank):
        do_trade(Items.Water_Tank)
        return True
    if not verify_quota(Items.Empty_Tank):
        trade(Items.Empty_Tank)
        return True
    return False


def do_carrot_trades():
    if not verify_quota(Items.Pumpkin_Seed):
        do_trade(Items.Pumpkin_Seed)
        return True
    if not verify_quota(Items.Sunflower_Seed):
        do_trade(Items.Sunflower_Seed)
        return True
    return False


def do_pumpkin_trades():
    if not verify_quota(Items.Fertilizer):
        do_trade(Items.Fertilizer)
        return True
    return False


def do_maze_trades():
    if not verify_quota(Items.Cactus_Seed):
        do_trade(Items.Cactus_Seed)
        return True
    return False


def do_cactus_trades():
    if not verify_quota(Items.Egg):
        do_trade(Items.Egg)
        return True
    return False
