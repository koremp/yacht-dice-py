import unittest
from yatch import four_of_a_kind, full_house, small_straight, large_straight, yacht


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


if __name__ == '__main__':
    unittest.main()
