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


def move_diff_vector(vector):
    move_diff(vector[0], vector[1])


def my_abs(a):
    if a > -1:
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


def opposite(direction):
    if direction == North:
        return South
    if direction == South:
        return North
    if direction == East:
        return West
    return East


def turn(direction):
    if direction == North:
        return East
    if direction == East:
        return South
    if direction == South:
        return West
    return North


def get_pos():
    return get_pos_x(), get_pos_y()


def apply_direction(position, direction):
    if direction == North:
        return position[0], position[1] + 1
    if direction == East:
        return position[0] + 1, position[1]
    if direction == South:
        return position[0], position[1] - 1
    return position[0] - 1, position[1]


def adjacent_tiles_of(pos):
    out = set()
    out.add((pos[0] + 1, pos[1]))
    out.add((pos[0] - 1, pos[1]))
    out.add((pos[0], pos[1] + 1))
    out.add((pos[0], pos[1] - 1))
    return out


def traverse_x(x):
    traverse(x, 0)


def traverse_y(y):
    traverse(0, y)

