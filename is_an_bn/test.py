from solution import is_an_bn

import unittest

class TestIsAnBn(unittest.TestCase):
    def test_is_an_bn(self):
        self.assertEqual(True, is_an_bn(""))
        self.assertEqual(False, is_an_bn("rado"))
        self.assertEqual(False, is_an_bn("aaabb"))
        self.assertEqual(True, is_an_bn("aaabbb"))
        self.assertEqual(False, is_an_bn("aabbaabb"))
        self.assertEqual(False, is_an_bn("bbbaaa"))
        self.assertEqual(True, is_an_bn("aaaaabbbbb"))

if __name__ == '__main__':
    unittest.main()
