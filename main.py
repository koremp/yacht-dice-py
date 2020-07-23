import os
import random
from yatch import four_of_a_kind, full_house, small_straight, large_straight, yacht

CATEGORY_NAME = ["Aces", "Duces", "Threes", "Fours", "Fives", "Sixes"]


def cls():
    os.system('cls' if os.name == 'nt' else 'clear')


def printSection(total_dice_list):
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


def main():
    field_dice_list = []
    saved_dice_list = []
    total_dice_list = []
    upper_section = [0 for x in range(6)]
    selected_upper_section = [0 for x in range(6)]
    fok, fh, ss, ls, yc = 0, 0, 0, 0, 0

    roll = 3
    upper_score = 0
    total_score = 0

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

    field_dice_list = total_dice_list

    while True:
        total_dice_list.sort()
        saved_dice_list.sort()
        field_dice_list.sort()
        print(f'Total Dice : {total_dice_list}')
        print(f'Saved Dice : {saved_dice_list}')
        print(f'Field Dice : {field_dice_list}')

        # input
        key = input('dice: d / Roll dice : r / Score : s / ')

        if key == 'd':
            while True:
                print()
                key1 = input(f'select dice num')

        elif key == 'r':
            dice_num = field_dice_list.len
            field_dice_list.clear()

            for x in range(dice_num):
                field_dice_list.append(random.randrange(1, 7))

        elif key == 's':
            saved_dice_list.append(field_dice_list.pop(2))


if __name__ == "__main__":
    main()
