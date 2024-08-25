from action_verifier import *
from trading import *

if get_entity_type() != Entities.Hedge:
    full_snake_path(harvest)
else:
    harvest()
clear()
while True:
    refresh_quotas()
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
    force_farm_entity(Entities.Treasure)
