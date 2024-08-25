from action_verifier import *
from trading import *

full_snake_path(harvest)
clear()
while True:
    try_farm_entity(Entities.Grass)
    try_farm_entity(Entities.Bush)
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
    force_farm_entity(Entities.Carrots)
