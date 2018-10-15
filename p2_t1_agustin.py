# @author: ajfernandez
# @last_edited: 12/10/18
# @repo: https://github.com/aj-fernandez/


i = 0
vow_cnt = 0
con_cnt = 0
vow_lst = ["a","e","i","o","u"]
con_lst = ["b","c","d","f","g","h","j","k","l","m","n","p","q","r","s","t","v"\
,"w","x","y","z"]

parag = str(input("Enter a paragraph: "))
parag = parag.lower()

while i < len(parag):
    if parag[i] in vow_lst:
        vow_cnt += 1
    elif parag[i] in con_lst:
        con_cnt += 1
    i += 1

print ("Number of words: %d\nVowels: %d\nConsonant: %d\nOther characters \
and spaces: %d" % (len(parag.split()), (vow_cnt), (con_cnt), (len(parag) -\
 (vow_cnt + con_cnt))))
