# @author: ajfernandez
# @last_edited: 12/10/18
# @repo: https://github.com/aj-fernandez/

import numpy as np

alphabet = ["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q"\
    ,"R","S","T","U","V","W","X","Y","Z"]

trit_max = np.empty([26,26], dtype = str)

for i in range(len(alphabet)):
    for col in range(len(alphabet)):
        for row in range(len(alphabet)):
            trit_max[row,col] = alphabet[i]
            
#trit_max = np.array([["a","b","c"],["d","e","f"],["g","h","i"]])

print(trit_max)
