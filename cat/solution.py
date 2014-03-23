import sys

def main():
    if(len(sys.argv)) > 1:
        file_name = sys.argv[1]
        file_handle = open(file_name, "r")
        content = file_handle.read()
        file_handle.close()
        return(content)
    else:
        return("No argument given")
