
# Donc on va coder le chiffrement de césar
# Tiens c'est marrant est-ce qu'il y a des structures de données circulaires ?
# On itère sur un string, ça c'est facile
# On bidouille l'index avec la clé
# Et paf c'est bon

def chiffrement_de_cesar(message:str, cle:int) -> str:

    alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    alpha_len = len(alphabet)

    if cle == alpha_len:
        return "zetes bourré"

    if cle > alpha_len:
        cle = cle % alpha_len

    message_chiffre = []
    for lettre in message:
        nouvel_index = alphabet.index(lettre) + cle
        if nouvel_index > alpha_len:
            nouvel_index = nouvel_index % alpha_len
        print(nouvel_index)
        message_chiffre.append(alphabet[nouvel_index - 1])
     
    return message_chiffre

user_message = "valoche"

# print(chiffrement_de_cesar(user_message, 19))
valochiffre = chiffrement_de_cesar(user_message, 19)

def dechiffrement_de_cesar(message:str, cle:int) -> str:

    alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    alpha_len = len(alphabet)

    if cle == alpha_len:
        return "zetes bourré"

    if cle > alpha_len:
        cle = cle % alpha_len
    
    message_dechiffre = []
    for lettre in message:
        nouvel_index = alphabet.index(lettre) + alpha_len - cle
        print(nouvel_index)
        message_dechiffre.append(alphabet[nouvel_index - 1])
    return message_dechiffre

print('______')
valodeschiffre = dechiffrement_de_cesar(valochiffre, 19)
print(valodeschiffre)
