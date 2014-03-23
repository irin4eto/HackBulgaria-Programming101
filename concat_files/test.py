import sys
import os
import unittest
import solution

class TestConcatFiles(unittest.TestCase):

    def setUp(self):
        sys.argv.append('testing1.txt')
        self.file_name1 = sys.argv[1]
        self.file_writing1 = open(self.file_name1, 'w')

        sys.argv.append('testing2.txt')
        self.file_name2 = sys.argv[2]
        self.file_writing2 = open(self.file_name2, 'w')

        self.new_file_name = "MEGATRON"

    def test_cat(self):
        self.file_writing1.write("Irina Ivanova\n")
        self.file_writing1.close()

        self.file_writing2.write("irina.bs@abv.bg\n")
        self.file_writing2.close()

        file_reading1 = open(self.file_name1, 'r')
        content1 = file_reading1.read()
        file_reading1.close()

        file_reading2 = open(self.file_name2, 'r')
        content2 = file_reading2.read()
        file_reading2.close()

        solution.main()

        new_file_reading = open(self.new_file_name, 'r')
        content_new_file = new_file_reading.read()
        new_file_reading.close()

        concat_content = content1 + content2

        self.assertEqual(concat_content, content_new_file)

        solution.main()

        new_file_reading = open(self.new_file_name, 'r')
        content_new_file = new_file_reading.read()
        new_file_reading.close()

        self.assertEqual(concat_content + concat_content, content_new_file)

    def tearDown(self):
        os.remove(self.file_name1)
        os.remove(self.file_name2)
        os.remove(self.new_file_name)

if __name__ == '__main__':
    unittest.main()
