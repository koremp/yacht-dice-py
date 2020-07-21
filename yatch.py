import random

CATEGORY_NAME = ["Aces", "Duces", "Threes", "Fours", "Fives", "Sixes"]


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


def full_house(li):
    fh = 0
    if li.count(1) == 2:
        if li.count(2) == 3:
            fh = sum(li)
        elif li.count(3) == 3:
            fh = sum(li)
        elif li.count(4) == 3:
            fh = sum(li)
        elif li.count(5) == 3:
            fh = sum(li)
        elif li.count(6) == 3:
            fh = sum(li)

    elif li.count(2) == 2:
        if li.count(1) == 3:
            fh = sum(li)
        elif li.count(3) == 3:
            fh = sum(li)
        elif li.count(4) == 3:
            fh = sum(li)
        elif li.count(5) == 3:
            fh = sum(li)
        elif li.count(6) == 3:
            fh = sum(li)

    elif li.count(3) == 2:
        if li.count(1) == 3:
            fh = sum(li)
        elif li.count(2) == 3:
            fh = sum(li)
        elif li.count(4) == 3:
            fh = sum(li)
        elif li.count(5) == 3:
            fh = sum(li)
        elif li.count(6) == 3:
            fh = sum(li)

    elif li.count(4) == 2:
        if li.count(1) == 3:
            fh = sum(li)
        elif li.count(2) == 3:
            fh = sum(li)
        elif li.count(3) == 3:
            fh = sum(li)
        elif li.count(5) == 3:
            fh = sum(li)
        elif li.count(6) == 3:
            fh = sum(li)

    elif li.count(5) == 2:
        if li.count(1) == 3:
            fh = sum(li)
        elif li.count(2) == 3:
            fh = sum(li)
        elif li.count(3) == 3:
            fh = sum(li)
        elif li.count(4) == 3:
            fh = sum(li)
        elif li.count(6) == 3:
            fh = sum(li)

    elif li.count(6) == 2:
        if li.count(1) == 3:
            fh = sum(li)
        elif li.count(2) == 3:
            fh = sum(li)
        elif li.count(3) == 3:
            fh = sum(li)
        elif li.count(4) == 3:
            fh = sum(li)
        elif li.count(5) == 3:
            fh = sum(li)

    return fh


def small_straight(li):
    ss = 0

    result = all(item in li for item in [1, 2, 3, 4]) or all(
        item in li for item in [2, 3, 4, 5]) or all(item in li for item in [3, 4, 5, 6])

    if result:
        ss = 15

    return ss


def large_straight(li):
    ls = 0

    if li == [1, 2, 3, 4, 5] or li == [2, 3, 4, 5, 6]:
        ls = 30

    return ls


def yacht(li):
    yc = 0

    if li[1:] == li[:-1]:
        yc = 50

    return yc


def main():
    field_dice_list = []
    saved_dice_list = []
    total_dice_list = []
    upper_section = [0 for x in range(6)]
    selected_upper_section = [0 for x in range(6)]
    fok, fh, ss, ls, yc = 0, 0, 0, 0, 0

    # roll dice
    for x in range(5):
        total_dice_list.append(random.randrange(1, 7))

    total_dice_list.sort()

    # calc upper section
    for dice in total_dice_list:
        if dice == 1:
            upper_section[0] = upper_section[0] + 1
        elif dice == 2:
            upper_section[1] = upper_section[1] + 1
        elif dice == 3:
            upper_section[2] = upper_section[2] + 1
        elif dice == 4:
            upper_section[3] = upper_section[3] + 1
        elif dice == 5:
            upper_section[4] = upper_section[4] + 1
        elif dice == 6:
            upper_section[5] = upper_section[5] + 1

    # calc lower section

    fok = four_of_a_kind(total_dice_list)
    fh = full_house(total_dice_list)
    ss = small_straight(total_dice_list)
    ls = large_straight(total_dice_list)
    yc = yacht(total_dice_list)

    # print upper section
    print("Num")
    for i in range(6):
        if selected_upper_section[i] == 0:
            print(f'{CATEGORY_NAME[i]} - {upper_section[i] * (i + 1)}')
        else:
            print(
                f'{CATEGORY_NAME[i]} - {selected_upper_section[i] * (i + 1)}')

    # print lower section
    print(f'Choices - {sum(total_dice_list)}')
    print(f'4 of a Kind - {fok}')
    print(f'Full House - {fh}')
    print(f'S. Straight - {ss}')
    print(f'L. Straight - {ls}')
    print(f'Yacht - {yc}')

    while True:
        key = input('1 ~ 5 to save dice / r to roll / s to score / ')

        if key == '1':
            saved_dice_list.append(field_dice_list.pop([0]))

        elif key == '2':
            saved_dice_list.append(field_dice_list.pop([1]))

        elif key == '3':
            saved_dice_list.append(field_dice_list.pop([2]))

        elif key == '4':
            saved_dice_list.append(field_dice_list.pop([3]))

        elif key == '5':
            saved_dice_list.append(field_dice_list.pop([4]))

        elif key == 'r':
            field_dice_num = len(field_dice_list)
            field_dice_list.clear()

            for x in range(field_dice_num):
                field_dice_list.append(random.range(1, 7))

        elif key == 's':
            '''  '''


if __name__ == '__main__':
    main()
