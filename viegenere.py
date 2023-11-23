
#So we are working on the vigenère cypher
#Which is an evolved form of the Cesar cypher
#So we have the text to encrypt, and we have the key
#Those would be the inputs of the program, the output is just the encrypted message
#Then the program needs a table of characters to reference
#Their indexes in the table will also be used

import string
import math

def vigenerization(message: str, key: str, decrypting: bool) -> str:

    chars = string.printable

    if len(message) < len(key):
        looping_factor = math.ceil( len(message) / len(key) )
        key = key * looping_factor

    numbered_key = []
    for char in key:
        char_index = chars.index(char)
        if char_index > len(chars) - 1:
            char_index = char_index % (len(chars) - 1)
        numbered_key.append(char_index)
    
    encrypted_message = []
    for char, tooth in zip(message, numbered_key):

        if decrypting:
            new_index = chars.index(char) - tooth
        else:
            new_index = chars.index(char) + tooth

        new_index = new_index % (len(chars) - 1)
        encrypted_message.append(chars[new_index])
    
    return encrypted_message

message = "Sois aussi pure que la neige, sois aussi chaste que la glace, tu n'échappera pas à la calomnie"
key = "rebondir"
print(vigenerization(message, key, False))

print(vigenerization(message, key, True))