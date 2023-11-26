import string

def cesar_ciffer(message, key):
	if type(key) != int :
		print("la clef doit être un entier")
		return None

	message = str(message)

	list_of_crypted_caracs = []
	
	for carac in message:
		crypted_index = (string.printable.index(carac) + key) % len(string.printable)
		crypted_carac = string.printable[crypted_index]
	
		list_of_crypted_caracs.append(crypted_carac)
	
	crypted_message = "".join(list_of_crypted_caracs)

	return crypted_message

def vigenere_ciffer(message, cle):
    list_of_key = [string.printable.index(password_carac) for password_carac in cle]
    list_of_crypted_carac = []

    for index_carac, carac in enumerate(message):
        current_key = list_of_key[index_carac % len(list_of_key)]
        list_of_crypted_carac.append(cesar_ciffer(carac, current_key))

    crypted_message = "".join(list_of_crypted_carac)
    return crypted_message

print (vigenere_ciffer(message = "hakim", cle = "abc"))

    