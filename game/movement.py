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


def calc_shortest(cur, dest):
    possibility1 = 0
    possibility2 = 0

    while (possibility1 + cur) % get_world_size() != dest:
        possibility1 += 1

    while (possibility2 + cur) % get_world_size() != dest:
        possibility2 -= 1

    if abs(possibility1) > abs(possibility2):
        return possibility2
    return possibility1


def traverse(dest_x, dest_y):
    move_diff(calc_shortest(get_pos_x(), dest_x), calc_shortest(get_pos_y(), dest_y))


def snake_path(action, initx, inity, width, height):
    traverse(initx, inity)
    right_bound = initx + width
    top_bound = inity + height
    for x in range(initx, right_bound + 1):
        if get_pos_y() == top_bound:
            while get_pos_y() != inity:
                action()
                move(South)
        else:
            while get_pos_y() != top_bound:
                action()
                move(North)
        if x != right_bound:
            action()
            move(East)
    action()


def full_snake_path(action):
    snake_path(action, 0, 0, get_world_size() - 1, get_world_size() - 1)
