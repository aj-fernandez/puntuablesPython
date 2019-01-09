
# @author: ajfernandez
# @last_edited: 09/01/19
# @repo: https://github.com/aj-fernandez/

coded_msg = ""
dcoded_msg = ""
msg = input("\nType a message: ").upper()
slider = int(input("\nEnter the value of key-slider: "))

for char in msg:
    if char == " ":
        coded_msg +=  char
    else:
        coded_msg += chr((ord(char) + slider - 65) % 26 + 65)

for char in coded_msg:
    if char == " ":
        dcoded_msg +=  char
    else:
        dcoded_msg += chr((ord(char) - slider - 65) % 26 + 65)

print("\n\nEncrypted message:", coded_msg)
print("\nDecrypted message:", dcoded_msg)
