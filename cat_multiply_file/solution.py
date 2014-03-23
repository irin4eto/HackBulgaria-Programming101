import sys

def main():
    if len(sys.argv) > 1:
        file_names = [sys.argv[i] for i in range(1, len(sys.argv))]
        result = ""
        for i in range(len(file_names)):
            file_handle = open(file_names[i], "r")
            result += file_handle.read() + '\n'
            file_handle.close()
        return result
    else:
        return "No argument given"
