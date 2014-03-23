from time import time
from datetime import datetime
import sys

current_dictionary = {}
save_dictionary = {}
filenames = []
last_save = False
get_list = False
count_load = 0
count_finish = 0


def finish():
    global last_save
    global count_finish
    if not last_save:
        count_finish += 1
        if count_finish == 2:
            print("Finishing order. Goodbye!")
            print("$")
            return True
        else :
            print("You have not saved your order")
            print("if you wish to continue, type finish again")
            print("If you want to save your order, type save")
            return False
    else:
        print("Finishing order. Goodbye!")
        print("$")
        return True
    return False

def input_choice():
    while True:
        choice = input("Enter command> ")
        choices = choice.split(" ")
        if choices[0] == "take":
            take(choices[1], int(choices[2]))
        elif choices[0] == "status":
            print(status())
        elif choices[0] == "save":
            save()
        elif choices[0] == "list":
            list_()
        elif choices[0] == "load":
            load(int(choices[1]))
        elif choices[0] == "finish":
            if finish():
                break
        else:
            print("Unknown command!\nTry one of the following:")
            print("take <name> <price>\nstatus\nsave\nlist")
            print("load <number>\nfinish\nEnter command>")



def take(choices1, choices2):
    print("Taking order from {} for {}".format(choices1, choices2))
    add_in_current_dictionary(choices1, choices2)
    global last_save
    last_save = False

def status():
    status_dictionary = {}
    for key in current_dictionary:
        if key in status_dictionary.keys():
            status_dictionary[key] = status_dictionary[key] + current_dictionary[key]
        else:
            status_dictionary[key] = current_dictionary[key]
    for key in save_dictionary:
        if key in status_dictionary.keys():
            status_dictionary[key] = status_dictionary[key] + save_dictionary[key]
        else:
            status_dictionary[key] = save_dictionary[key]
    result = ""
    for key in status_dictionary:
        result = result + "{} - {}\n".format(key, status_dictionary[key])
    return result

def save():
    global last_save
    global filenames
    ts = time()
    stamp = datetime.fromtimestamp(ts).strftime('%Y_%m_%d_%H_%M_%S')
    filenames.append("orders_%s" %(stamp))
    if len(filenames) != 1:
        store = filenames[len(filenames) - 1]
        count = len(filenames) - 1
        while count != 0:
            filenames[count] = filenames[count - 1]
            count -= 1
        filenames[0] = store
    file = open(filenames[0], "w")
    file.write(status())
    print("Saved the current order to {}".format(filenames[0]))
    add_in_save_dictionary()
    last_save = True
    current_dictionary.clear()

def list_():
    global get_list
    get_list = True
    for i in range(len(filenames)):
        print("[{}] - {}".format(i + 1, filenames[i]))

def load(number):
    global get_list
    global count_load
    if not get_list:
        print("Use list command before loading")
    elif not last_save:
        count_load += 1
        if count_load == 1:
            print("You have not saved current order.")
            print("If you wish to discard it, type load")
        if count_load == 2:
            load_number(number)
    else:
        load_number(number)

def load_number(number):
    global count_load
    count_load = 0
    count_filenames = 0
    for i in range(number - 1, len(filenames)):
        filenames[count_filenames] = filenames[i]
        count_filenames += 1
    for i in range(len(filenames)):
        filenames[count_filenames] = None
    file = open(filenames[0], 'r')
    read_dictionary = {}
    for line in file:
        read_dictionary[list(line.strip().split(" "))[0]] = list(line.strip().split(" "))[2]
    delete_elem = []
    for key in save_dictionary:
        if key in read_dictionary.keys():
            save_dictionary[key] = read_dictionary[key]
        else:
            delete_elem.append(key)
    for key in delete_elem:
        del save_dictionary[key]

def add_in_current_dictionary(names, money):
    if names in current_dictionary.keys():
        current_dictionary[names] += money
    else:
        current_dictionary[names] = money

def add_in_save_dictionary():
    for i in current_dictionary:
        if i in save_dictionary.keys():
            save_dictionary[i] += current_dictionary[i]
        else:
            save_dictionary[i] = current_dictionary[i]

def main():
    input_choice()
if __name__ == '__main__':
    main()
