import random


def four_of_a_kind(dice_list):
    fok = 0

    if dice_list.count(1) >= 4:
        fok = 1 * dice_list.count(1)
    elif dice_list.count(2) >= 4:
        fok = 2 * dice_list.count(2)
    elif dice_list.count(3) >= 4:
        fok = 3 * dice_list.count(3)
    elif dice_list.count(4) >= 4:
        fok = 4 * dice_list.count(4)
    elif dice_list.count(5) >= 4:
        fok = 5 * dice_list.count(5)
    elif dice_list.count(6) >= 4:
        fok = 6 * dice_list.count(6)

    return fok


def full_house(dice_list):
    fh = 0
    if dice_list.count(1) == 2:
        if dice_list.count(2) == 3:
            fh = sum(dice_list)
        elif dice_list.count(3) == 3:
            fh = sum(dice_list)
        elif dice_list.count(4) == 3:
            fh = sum(dice_list)
        elif dice_list.count(5) == 3:
            fh = sum(dice_list)
        elif dice_list.count(6) == 3:
            fh = sum(dice_list)

    elif dice_list.count(2) == 2:
        if dice_list.count(1) == 3:
            fh = sum(dice_list)
        elif dice_list.count(3) == 3:
            fh = sum(dice_list)
        elif dice_list.count(4) == 3:
            fh = sum(dice_list)
        elif dice_list.count(5) == 3:
            fh = sum(dice_list)
        elif dice_list.count(6) == 3:
            fh = sum(dice_list)

    elif dice_list.count(3) == 2:
        if dice_list.count(1) == 3:
            fh = sum(dice_list)
        elif dice_list.count(2) == 3:
            fh = sum(dice_list)
        elif dice_list.count(4) == 3:
            fh = sum(dice_list)
        elif dice_list.count(5) == 3:
            fh = sum(dice_list)
        elif dice_list.count(6) == 3:
            fh = sum(dice_list)

    elif dice_list.count(4) == 2:
        if dice_list.count(1) == 3:
            fh = sum(dice_list)
        elif dice_list.count(2) == 3:
            fh = sum(dice_list)
        elif dice_list.count(3) == 3:
            fh = sum(dice_list)
        elif dice_list.count(5) == 3:
            fh = sum(dice_list)
        elif dice_list.count(6) == 3:
            fh = sum(dice_list)

    elif dice_list.count(5) == 2:
        if dice_list.count(1) == 3:
            fh = sum(dice_list)
        elif dice_list.count(2) == 3:
            fh = sum(dice_list)
        elif dice_list.count(3) == 3:
            fh = sum(dice_list)
        elif dice_list.count(4) == 3:
            fh = sum(dice_list)
        elif dice_list.count(6) == 3:
            fh = sum(dice_list)

    elif dice_list.count(6) == 2:
        if dice_list.count(1) == 3:
            fh = sum(dice_list)
        elif dice_list.count(2) == 3:
            fh = sum(dice_list)
        elif dice_list.count(3) == 3:
            fh = sum(dice_list)
        elif dice_list.count(4) == 3:
            fh = sum(dice_list)
        elif dice_list.count(5) == 3:
            fh = sum(dice_list)

    return fh


def small_straight(dice_list):
    ss = 0

    result = all(item in dice_list for item in [1, 2, 3, 4]) or all(
        item in dice_list for item in [2, 3, 4, 5]) or all(item in dice_list for item in [3, 4, 5, 6])

    if result:
        ss = 15

    return ss


def large_straight(dice_list):
    ls = 0

    if dice_list == [1, 2, 3, 4, 5] or dice_list == [2, 3, 4, 5, 6]:
        ls = 30

    return ls


def yacht(dice_list):
    yc = 0

    if dice_list[1:] == dice_list[:-1]:
        yc = 50

    return yc
