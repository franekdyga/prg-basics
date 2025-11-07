###
# Encrypts text using Caesar Code, shifting each letter
# in the alphabet right one position
#
plain_text = 'The early bird catches the worm'
encrypted_text = ''

# x = ord(' ')
# print(x)
# x = x+1
# y = chr(x)
# print(y)

for char in plain_text:
    # read the character's code (use ord())
    a = ord(char)
    # add one to the character's code
    if a == 32:
        pass
    else:
        a = a+1
    # replace new character code with its
    # corresponding character (use chr())

    a = chr(a)
    # add encrypted character to encrypted text
    encrypted_text = encrypted_text + a

print(plain_text)
print(encrypted_text)