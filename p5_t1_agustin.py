# @author: ajfernandez
# @last_edited: 25/11/18
# @repo: https://github.com/aj-fernandez/

def loadData():

    myDict = {}

    target = input("Enter the name of the file: ")

    with open(target) as source:
        for line in source:
            key, value = line.strip().split(',', maxsplit=1) # 1 delimiter per line
            myDict[key] = value.strip() # With strip() we remove the spaces at
                                        # beginning or end of the string

    print(myDict)
    print("\n")
    menu()

def saveData():

    regNumber = int(input("Enter the number of pairs [key, value] that you want to save: "))

    newDict = {}
    for i in range (regNumber):
        key = input("Enter the key: ").strip()
        value = input("Enter her value: ").strip()
        newDict[key] = value

    print("\nThe generated dictionary is:\n ")
    print(newDict)

    newFile = input("Enter a new name file to save this dictionary: ")

    records = newDict.items()

    with open(newFile, "w") as target:
        for key, value in records:
            target.write(str(key + ", " + value + "\n"))

    menu()

def out():

    print("\nBye bye!!\n")
    exit(0)

def menu():

    print("\n1. To generate a dictionary from file (LOAD DATA).\n2. To generate \
a file from dictionary (SAVE DATA).\n3. Exit.")
    argument = int(input())
    switcher = {
        1: loadData,
        2: saveData,
        3: out,
    }
    func = switcher.get(argument, lambda: menu())
    func()
menu()
