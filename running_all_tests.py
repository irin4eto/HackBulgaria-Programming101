import glob
from subprocess import call

def main():
    for dirr in glob.glob("*[!.]??"):
        if dirr != 'generate_numbers' and dirr != 'pizza':
            print("\ntests for {}".format(dirr))
            call("python3.3 ./{}/test.py".format(dirr), shell = True)

if __name__ == '__main__':
    main()
