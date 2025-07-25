def generate_key(n):
	"""
	generate_key(n)
	Fonction qui génère une clé pour le chiffrement
	On passe un entier qui est en fait la vraie clé.
	Paramètres:
	n (int) : entier, clé de chiffrement
	
	Return
	Dictionnaire : la clé de mappage
	"""
	# Lettres utilisées pour le mappage
	letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
	
	# Nous allons utiliser un dictionnaire pour faire le mappage
	key = {}
	cnt = 0
	
	# Génère la clé
	for c in letters:
		# Le modulo permet de gérer un nombre qui déborde du nombre de lettre
		# Le modulo permet de redémarrer au début si la valeur de c est
		# plus grande que 25
		key[c] = letters[(cnt + n) % len(letters)]
		cnt += 1
	
	return key

# Vérifions que notre clé est bien générée
key = generate_key(3)
print(key)


def encrypt(key, message):

	"""
	encrypt(key, message)
	Fonction qui chiffre le message.
	
	Paramètres :
	key (dict): clé de mappage.
	message (string): mesage à chiffrer

	Return :
	string : le message chiffré
	"""
	
	# Va contenir le message chiffré
	secret = ""
	
	# Vous devez créer une boucle for qui vérifie si le caractère est dans
	# dans la clé de mappage. Si oui, on le substitue. Sinon, on le
	# le remet tel quel.
	for c in message:
		if c in key:
			secret += key[c]
		else:
			secret += c
	return secret

# Vérifions que notre clé est bien générée
key = generate_key(3)
print(key)

# Genere la clé de chiffrement
def generate_dkey(key):
	dkey = {}
	for c in key:
		dkey[key[c]]=c
	return dkey

# Vérifions que le chiffrement fonctionne
message = "AINSI VA LA VIE"
secret = encrypt(key, message)
print("message chiffré :",secret)

# on essaye de déchiffrer avec la clé de mappage (on chiffre à nouveau mais cela ne fonctionne pas)
message = encrypt(key, secret)
print (message)

# On génère une clé de mappage différente pour chiffrer
dkey = generate_dkey(key)
message = encrypt(dkey, secret)
print ("message déchiffré :", message)

# Attaque sur le chiffrement de César
print("####################################")
print("Attaque sur le chiffrement de César")
for i in range(26):
	dkey = generate_key(i)
	message = encrypt(dkey, secret)
	print(message)
print("####################################")