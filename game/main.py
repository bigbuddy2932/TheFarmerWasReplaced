from action_verifier import *
from trading import *

if get_entity_type() != Entities.Hedge:
    full_snake_path(harvest)
else:
    harvest()
clear()
while True:
    set_execution_speed(20)
    refresh_quotas()
    try_auto_unlock()
    try_farm_entity(Entities.Grass)
    try_farm_entity(Entities.Tree)
    if do_wood_trades():
        continue
    if try_farm_entity(Entities.Carrots):
        continue
    if do_carrot_trades():
        continue
    if try_farm_entity(Entities.Pumpkin):
        continue
    if do_pumpkin_trades():
        continue
    if try_farm_entity(Entities.Sunflower):
        continue
    if try_farm_entity(Entities.Treasure):
        continue
    if do_maze_trades():
        continue
    if try_farm_entity(Entities.Cactus):
        continue
    if do_cactus_trades():
        continue
    try_auto_unlock()
    force_farm_entity(Entities.Cactus)
