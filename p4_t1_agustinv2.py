# @author: ajfernandez
# @last_edited: 16/11/18
# @repo: https://github.com/aj-fernandez/

# -*- coding: utf-8 -*-

import numpy as np

def new_matrix(msg):

    alphabet = ["A","B","C","D","E","F","G","H","I","J","K","L","M","N", "Ñ", "O","P","Q"\
        ,"R","S","T","U","V","W","X","Y","Z"]  # trit_max[i,j] = alphabet[(i+j)%len(alphabet)] if alphabet were a string or
                                               # can use ASCII 65 - 90
                                               # TODO: try both []

    trit_matrix = np.empty([27,27], dtype = str)

    for i in range(len(alphabet)):
        for j in range(len(alphabet)):
                trit_matrix[i,j] = alphabet[(i+j)%len(alphabet)]

    trit_matrix.tolist()

    code(trit_matrix,msg)

def code(matrix,msg):

    coded_msg =  ""
    spaces = 0

    coded_msg += msg[0]

    for j in range(1, len(msg)):
                if msg[j] == " ":
                    coded_msg += " "
                    spaces += 1
                else:
                    for i in range(0, 27):
                        if msg[j] == matrix[i,0]:
                            coded_msg += matrix[i,(j - spaces)]

    print("\nCoded message is:\n")
    print(coded_msg)

    decode(matrix, coded_msg)

def decode(matrix,msg):

    decoded_msg =  ""
    spaces = 0

    decoded_msg += msg[0]

    for j in range(1, len(msg)):
                if msg[j] == " ":
                    decoded_msg += " "
                    spaces += 1
                else:
                    for i in range(0, 27):
                        if msg[j] == matrix[i,0]:
                            decoded_msg += matrix[i,((27 - j) + spaces)]

    print("\nDecoded message is:\n")
    print(decoded_msg)


def main():

    msg = input("Enter a message to be encrypted: ")
    msg = msg.upper()

    new_matrix(msg)

main()
