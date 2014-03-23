import unittest
import sys
import os
import solution


class TestCatMultiplyFile(unittest.TestCase):

    def setUp(self):
        sys.argv.append('testing1.txt')
        self.file_name1 = sys.argv[1]
        self.file_writing1 = open(self.file_name1, 'w')

        sys.argv.append('testing2.txt')
        self.file_name2 = sys.argv[2]
        self.file_writing2 = open(self.file_name2, 'w')

    def test_cat(self):
        self.file_writing1.write("Irina Ivanova")
        self.file_writing1.close()

        self.file_writing2.write("irina.bs@abv.bg")
        self.file_writing2.close()

        file_reading1 = open(self.file_name1, "r")
        content1 = file_reading1.read()
        file_reading1.close()

        file_reading2 = open(self.file_name2, "r")
        content2 = file_reading2.read()
        file_reading2.close()

        result = content1 + '\n' + content2 + '\n'

        self.assertEqual(result, solution.main())

    def tearDown(self):
        os.remove(self.file_name1)
        os.remove(self.file_name2)


if __name__ == '__main__':
    unittest.main()
