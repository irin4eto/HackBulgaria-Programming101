import sys
import os
import unittest
import solution

class TestSumIntegers(unittest.TestCase):

    def setUp(self):
        sys.argv.append("testing.txt")
        self.file_name = sys.argv[1]
        self.file_writing = open(self.file_name, 'w')

    def test_sum_integers(self):
        self.file_writing.write("10 345 23 67 89")
        self.file_writing.close()

        self.assertEqual(534, solution.main())

    def tearDown(self):
        os.remove(self.file_name)

if __name__ == '__main__':
    unittest.main()
