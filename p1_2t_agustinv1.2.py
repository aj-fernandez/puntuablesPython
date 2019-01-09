coded_msg = ""

msg = input("\nType a message: ").upper()
slider = int(input("\nEnter the value of key-slider: "))

for char in msg:
    if char == " ":
        coded_msg +=  char
    else:
        coded_msg += chr((ord(char) + slider - 65) % 26 + 65)

print("\n\nEncrypted message:", coded_msg)

