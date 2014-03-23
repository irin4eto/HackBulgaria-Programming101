import unittest
import sys
import os
import solution


class TestCat(unittest.TestCase):

    def setUp(self):
        sys.argv.append('testting.txt')
        self.file_name = sys.argv[1]
        self.file_writing = open(self.file_name, "w")

    def test_cat(self):
        self.file_writing.write("Irina Ivanova")
        self.file_writing.close()

        file_reading = open(self.file_name, "r")
        content = file_reading.read()
        file_reading.close()

        self.assertEqual(content, solution.main())

    def tearDown(self):
        os.remove(self.file_name)


if __name__ == '__main__':
    unittest.main()
