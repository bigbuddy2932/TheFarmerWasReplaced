from __builtins__ import *


def move_diff(mov_x, mov_y):
    while mov_x > 0:
        move(East)
        mov_x -= 1
    while mov_x < 0:
        move(West)
        mov_x += 1
    while mov_y > 0:
        move(North)
        mov_y -= 1
    while mov_y < 0:
        move(South)
        mov_y += 1


def my_min(a, b):
    if a > b:
        return b
    return a


def my_max(a, b):
    if a > b:
        return b
    return a


def my_abs(a):
    if a > 0:
        return a
    return a * -1


def calc_shortest(cur, dest):
    possibility1 = 0
    possibility2 = 0

    while (possibility1 + cur) % get_world_size() != dest:
        possibility1 += 1

    while (possibility2 + cur) % get_world_size() != dest:
        possibility2 -= 1

    if my_abs(possibility1) > my_abs(possibility2):
        return possibility2
    return possibility1


def traverse(dest_x, dest_y):
    move_diff(calc_shortest(get_pos_x(), dest_x), calc_shortest(get_pos_y(), dest_y))
