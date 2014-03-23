import sys
import unittest
import os
import solution

class TestWc(unittest.TestCase):

    def setUp(self):
        sys.argv.append("lines")
        sys.argv.append("testing.txt")
        self.file_name = sys.argv[2]
        self.file_handle = open(self.file_name, 'w')

    def test_wc(self):
        self.file_handle.write("Irina Ivanova\nirina.bs@abv.bg")
        self.file_handle.close()

        self.assertEqual(2, solution.main())

        sys.argv[1] = "words"
        self.assertEqual(3, solution.main())

        sys.argv[1] = "chars"
        self.assertEqual(29, solution.main())

    def tearDown(self):
        os.remove(self.file_name)

if __name__ == '__main__':
    unittest.main()
