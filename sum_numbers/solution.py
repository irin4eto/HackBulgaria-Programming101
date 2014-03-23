import sys

def main():
    if len(sys.argv) > 0:
        file_name = sys.argv[1]
        file_handle = open(file_name, "r")
        contents = file_handle.read().strip().split(" ")
        file_handle.close()
        return sum(list(map(int, contents)))
    else:
        return "No valid argument"
