# @author: ajfernandez
# @last_edited: 12/10/18
# @repo: https://github.com/aj-fernandez/

myDict = dict()
letras = myDict.keys()
uppercase = range(65,90)
lowercase = range(97,122)
for i in uppercase:
    myDict[str(i)] = chr(i)
for j in lowercase:
    myDict[str(j)] = chr(j)
for keys in myDict:
    print(keys, "-", myDict[keys])
