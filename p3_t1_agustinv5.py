# @author: ajfernandez
# @last_edited: 8/11/18
# @repo: https://github.com/aj-fernandez/


argument = 0

def cal():
    lst = ["T","R","W","A","G","M","Y","F","P","D","X","B","N","J","Z","S","Q"\
    ,"V","H","L","C","K","E"]
    i = 0

    dni = int(input("Enter your DNI digits: ")) #TODO: dni MUST have 8 digits, check it! [OK]

    while  len(str(dni)) != 8 and i < 2:
        print ("The number isnt valid, this must match with 8 digits")
        dni = int(input("Enter your DNI digits: "))
        i += 1
    else:                                       #TODO: check if something isnt a digit []
        if i == 2:
            print ("You have entered 3 invalid numbers, bye bye!!")
            out()
        else:
            pass # when statement is required but not need code, "continue" goes
                 # to the begining of while again.

    mod = dni % 23
    let = lst[mod]

    if argument == 1:
        show_letter(let)
    else:
        let_in = str(input("Enter your letter: "))
        let_in = let_in.upper()
        check(let,let_in)

def show_letter(a):
    print ("\nAccording to the digits the letter is: %s" %(a))
    menu()

def check(a,b):
    if a != b:
        print ("Wrong input letter, your correct letter is: %s" %(a))
    else:
        print ("All is OK!")

    menu()

def out():
    print ("Bye bye!!")
    exit(0)

def menu():
    global argument
    print ("\n1. To generate the letter of DNI.\n2. To check DNI letter.\n3. Exit.")
    argument = int(input())
    switcher = {
        1: cal,
        2: cal,
        3: out,
    }
    func = switcher.get(argument, lambda: menu())
    func()
menu()
