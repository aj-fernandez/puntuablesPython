#!/usr/bin/python

argument = 0

def cal():
    lst = ["T","R","W","A","G","M","Y","F","P","D","X","B","N","J","Z","S","Q"\
    ,"V","H","L","C","K","E"]

    dni = int(raw_input("Enter a DNI number: ")) #TODO: dni MUST have 8 digits, check it!

    mod = dni % 23
    let = lst[mod]

    if argument == 1:
        show_letter(let)
    else:
        let_in = raw_input("Enter the letter: ")
        let_in = let_in.upper()
        check(let,let_in)

def show_letter(a):
    print "\nAccording to the number the letter is: ", a
    menu()

def check(a,b):
    if a != b:
        print "Your input letter fails, really is: ", a
    else:
        print "All is OK!"

    menu()

def out():
    print "Bye bye!!"

def menu():
    global argument
    print "\n1. To generate the letter of DNI.\n2. To check NDNI letter.\n3. Exit."
    argument = int(raw_input())
    switcher = {
        1: cal,
        2: cal,
        3: out,
    }
    func = switcher.get(argument, lambda: menu())
    func()
menu()
