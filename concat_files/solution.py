import sys

def main():
    new_file_name = "MEGATRON"
    if len(sys.argv) > 1:
        file_names = [sys.argv[i] for i in range(1, len(sys.argv))]
        file_handle_new_file = open(new_file_name, "a")
        for i in file_names:
            file_handle = open(i, "r")
            file_handle_new_file.write(file_handle.read())
            file_handle.close()
        file_handle_new_file.close()
    else:
        return "No argument given"
