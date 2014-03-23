from random import randint
import sys

def main():
    if len(sys.argv) > 1:
        file_name = sys.argv[1]
        number = int(sys.argv[2])
        file_handle = open(file_name, "w")
        for i in range(number):
            file_handle.write(str(randint(1, 50)))
            file_handle.write(" ")
        return file_handle.read().split()
    else:
        return " No generate argument"
