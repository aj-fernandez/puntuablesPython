# @author: ajfernandez
# @last_edited: 12/10/18
# @repo: https://github.com/aj-fernandez/


def calDNI():
    lst = ["T","R","W","A","G","M","Y","F","P","D","X","B","N","J","Z","S","Q"\
    ,"V","H","L","C","K","E"]


    n = int(raw_input("Introduzca el numero del DNI"))

    mod = num%23
    let = lst[mod]

    print "Letra:", let


print "1. Para generar la letra del DNI.\n2. Para validar la letra del DNI.\n\
3. Salir."

ch = raw_input()

def myswitch(ch):
    lst = ["T","R","W","A","G","M","Y","F","P","D","X","B","N","J","Z","S","Q"\
    ,"V","H","L","C","K","E"]
    return {
        1 : lambda x: let = lst[mod],
        2 : lambda x: x*2,
        3 : lambda x: x-123,
    }.get(value)(x)

    n = int(raw_input("Introduzca el numero del DNI"))

print "The result for inp is : ", # myswitch(n)) basuraaaaaaaa!!!, i will continue to v2
