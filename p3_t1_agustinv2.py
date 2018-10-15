# @author: ajfernandez
# @last_edited: 12/10/18
# @repo: https://github.com/aj-fernandez/


def calDNI():
    lst = ["T","R","W","A","G","M","Y","F","P","D","X","B","N","J","Z","S","Q"\
    ,"V","H","L","C","K","E"]

    dni = int(raw_input("Enter a DNI number: ")) #TODO: dni MUST have 8 digits, check it!

    mod = dni % 23
    let = lst[mod]

    print "According to the number the letter is: ", let
    driven()

def check():
    lst = ["T","R","W","A","G","M","Y","F","P","D","X","B","N","J","Z","S","Q"\
    ,"V","H","L","C","K","E"]

    dni = int(raw_input("Enter a DNI number: "))
    let = raw_input("Enter the letter: ")
    let = let.upper()

    mod = dni % 23
    truelet = lst[mod]

    if let != truelet:
        print "Your input letter fails, really is: ", truelet
    else:
        print "All is OK!"

    driven()

def out():
    print "Adios."

def menu(argument):
    switcher = {
        "1": calDNI,
        "2": check,
        "3": out,

    }
    func = switcher.get(argument, lambda: driven())
    func()

def driven():
    print "\n1. Para generar la letra del DNI.\n2. Para validar la letra del DNI.\
    \n3. Salir."

    argument = raw_input()

    menu(argument)

driven()
