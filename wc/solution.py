import sys

def main():
    if len(sys.argv) > 1:
        file_name = sys.argv[2]
        file_handle = open(file_name, "r")

        if sys.argv[1] == "lines":
            count_lines = len([x for x in file_handle.read().split('\n')])
            file_handle.close()
            return count_lines

        if sys.argv[1] == "chars":
            count_chars = len([x for x in file_handle.read() if type(x) == str])
            file_handle.close()
            return count_chars

        if sys.argv[1] == "words":
            count_words = len([x for x in file_handle.read().split()])
            file_handle.close()
            return count_words

    else:
        return "No argument given"
