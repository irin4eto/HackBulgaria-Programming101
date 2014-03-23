import unittest

from solution import nth_fibonacci

class TestNthFibonacci(unittest.TestCase):
    def test_nth_fibonacci(self):
        self.assertEqual(1, nth_fibonacci(1))
        self.assertEqual(1, nth_fibonacci(2))
        self.assertEqual(2, nth_fibonacci(3))
        self.assertEqual(55, nth_fibonacci(10))

if __name__ == '__main__':
    unittest.main()
