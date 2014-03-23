import unittest

from solution import prime_number_of_divisors
from solution import is_prime

class TestPrimeNumberOfDivisors(unittest.TestCase):
    def test_prime_number_of_divisors(self):
        self.assertEqual(True, prime_number_of_divisors(7))
        self.assertEqual(False, prime_number_of_divisors(8))
        self.assertEqual(True, prime_number_of_divisors(9))

    def test_is_prime(self):
        self.assertEqual(False, is_prime(1))
        self.assertEqual(True, is_prime(2))
        self.assertEqual(False, is_prime(8))
        self.assertEqual(True, is_prime(11))
        self.assertEqual(False, is_prime(-10))

if __name__ == '__main__':
    unittest.main()
