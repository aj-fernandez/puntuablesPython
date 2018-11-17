# @author: ajfernandez
# @last_edited: 12/10/18
# @repo: https://github.com/aj-fernandez/

import numpy as np

def new_matrix(msg):

    alphabet = ["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q"\
        ,"R","S","T","U","V","W","X","Y","Z"]  # trit_max[i,j] = alphabet[(i+j)%len(alphabet)] if alphabet were a string or
                                               # can use ASCII 65 - 90
                                               # TODO: try both []

    trit_matrix = np.empty([26,26], dtype = str)

    for i in range(len(alphabet)):
        for j in range(len(alphabet)):
                trit_matrix[i,j] = alphabet[(i+j)%len(alphabet)]

    print(trit_matrix)

    code(trit_matrix,msg)

def code(matrix,msg):

    coded_msg = []
    col_matrix = 0
    row_matrix = 0

    for l in range(len(msg)):
        for i in msg[l]:
            #print(i) i toma el valor de cada letra de la palabra
            for j in matrix[col_matrix,row_matrix]:
                print(j)
                # col_matrix = col_matrix + 1
                # row_matrix = row_matrix + 1
                if i == j:
                    coded_msg.append(j)
                # else:
                #     col_matrix = col_matrix + 1
                #     row_matrix = row_matrix + 1




    print("Coded message is:\n")
    print(coded_msg)

#def decode():

def main():

    msg = input("Enter a message to be encrypted: ")
    msg = msg.upper()

    new_matrix(msg)


main()
