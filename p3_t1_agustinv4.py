#!/usr/bin/python

argument = 0

def cal():
    lst = ["T","R","W","A","G","M","Y","F","P","D","X","B","N","J","Z","S","Q"\
    ,"V","H","L","C","K","E"]

    dni = int(input("Enter your DNI digits: ")) #TODO: dni MUST have 8 digits, check it!

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

def menu():
    global argument
    print ("\n1. To generate the letter of DNI.\n2. To check NDNI letter.\n3. Exit.")
    argument = int(input())
    switcher = {
        1: cal,
        2: cal,
        3: out,
    }
    func = switcher.get(argument, lambda: menu())
    func()
menu()
