# @author: ajfernandez
# @last_edited: 12/10/18
# @repo: https://github.com/aj-fernandez/


myDict = dict()
uppercase = range(65,90)
lowercase = range(97,122)
for i in uppercase:
    myDict[str(i)] = chr(i)
for j in lowercase:
    myDict[str(j)] = chr(j)
for key, value in sorted(myDict.items(), key=lambda ab: (ab[1], ab[0])):
    print (key, "-", value)



#for keys in sorted(myDict):
#    print keys, "-", myDict[keys]
#
#   TODO: El comentado no termina de ordenarlo bien. fix it!!            []
#   TODO: buscar info sobre OrderedDict (modulo) y probar               [OK]
#
