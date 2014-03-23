import unittest

from solution import calculate_coins

class TestCalculateCoins(unittest.TestCase):
    def test_calculate_coins(self):
        self.assertDictEqual({1: 1, 2: 1, 100: 0, 5: 0, 20: 0, 10: 0, 50: 1}, calculate_coins(0.53))
        self.assertDictEqual({1: 0, 2: 2, 100: 8, 5: 0, 20: 2, 10: 0, 50: 1}, calculate_coins(8.94))

if __name__ == '__main__':
    unittest.main()
