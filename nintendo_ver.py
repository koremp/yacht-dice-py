import random
import unittest
from collections import Counter

CATEGORY_NAME = ["Aces", "Duces", "Threes", "Fours", "Fives", "Sixes"]


class lowerSectionTest(unittest.TestCase):
    def test_four_of_a_Kind(self):
        self.assertEqual(four_of_a_kind([1, 1, 1, 1, 1]), 5)
        self.assertEqual(four_of_a_kind([1, 1, 1, 1, 2]), 4)
        self.assertEqual(four_of_a_kind([2, 2, 2, 2, 2]), 10)
        self.assertEqual(four_of_a_kind([2, 2, 2, 2, 3]), 8)
        self.assertEqual(four_of_a_kind([3, 3, 3, 3, 3]), 15)
        self.assertEqual(four_of_a_kind([3, 3, 3, 3, 4]), 12)

    def test_FullHouse(self):
        self.assertEqual(full_house([1, 1, 1, 2, 2]), sum([1, 1, 1, 2, 2]))

    def test_SmallStraight(self):
        self.assertEqual(small_straight([1, 2, 3, 4, 5]), 15)
        self.assertEqual(small_straight([1, 2, 3, 4, 6]), 15)
        self.assertEqual(small_straight([2, 3, 4, 5, 6]), 15)

        self.assertEqual(small_straight([1, 1, 1, 1, 1]), 0)

    def test_LargeStraight(self):
        self.assertEqual(large_straight([1, 2, 3, 4, 5]), 30)
        self.assertEqual(large_straight([2, 3, 4, 5, 6]), 30)

        self.assertEqual(large_straight([1, 1, 1, 1, 1]), 0)

    def test_Yacht(self):
        self.assertEqual(yacht([1, 1, 1, 1, 1]), 50)
        self.assertEqual(yacht([2, 2, 2, 2, 2]), 50)
        self.assertEqual(yacht([3, 3, 3, 3, 3]), 50)
        self.assertEqual(yacht([4, 4, 4, 4, 4]), 50)
        self.assertEqual(yacht([5, 5, 5, 5, 5]), 50)
        self.assertEqual(yacht([6, 6, 6, 6, 6]), 50)

        self.assertEqual(yacht([1, 1, 1, 1, 2]), 0)


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

    else:
        fh = 0

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
    li = []
    categories = [0 for x in range(6)]
    selected_categories = [0 for x in range(6)]
    fok, fh, ss, ls, yc = 0, 0, 0, 0, 0

    # roll dice
    for x in range(5):
        li.append(random.randrange(1, 7))

    li.sort()

    # calc upper section
    for item in li:
        if item == 1:
            categories[0] = categories[0] + 1
        elif item == 2:
            categories[1] = categories[1] + 1
        elif item == 3:
            categories[2] = categories[2] + 1
        elif item == 4:
            categories[3] = categories[3] + 1
        elif item == 5:
            categories[4] = categories[4] + 1
        elif item == 6:
            categories[5] = categories[5] + 1

    # calc lower section

    fok = four_of_a_kind(li)
    fh = full_house(li)
    ss = small_straight(li)
    ls = large_straight(li)
    yc = yacht(li)

    # print upper section
    print("Num")
    for i in range(6):
        if selected_categories[i] == 0:
            print(f'{CATEGORY_NAME[i]} - {categories[i] * (i + 1)}')
        else:
            print(f'{CATEGORY_NAME[i]} - {selected_categories[i] * (i + 1)}')

    # print lower section
    print(f'Choices - {sum(li)}')
    print(f'4 of a Kind - {fok}')
    print(f'Full House - {fh}')
    print(f'S. Straight - {ss}')
    print(f'L. Straight - {ls}')
    print(f'Yacht - {yc}')

    print('select dice')
    print('rolls remained -')


main()
