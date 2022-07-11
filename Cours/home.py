from ast import keyword
import random
from zipfile import BadZipFile

#firstname = Prénom
#lastname = Nom
#number = Nombre
#email = Mail ou Gmail 
#New_emails = Nouveaux email 
firstname = "toto"
lastname = "pop"
number = random.randint(2, 10)

email = firstname + '.' + lastname + str(number) + '@example.com'
print(email)


new_emails = random.randint(0, 3)

if new_emails == 0:
    pass
    print("Vous navez pas de nouveaux mail")
elif new_emails == 1:
    print("Vous avez reçu <strong>1</strong> nouveau mail")
else:
    print("Vous avez reçu <strong>" + str (new_emails) + "</strong> nouveaux mails")


stock = random.randint(0, 15)


if stock == 0:
    print("Stock épusie")
elif stock == 1:
    print("Stock en tension : 1 piece")
elif 1 < stock < 5:
    print(f"Stock en tension : {stock} pieces")
elif 5 <= stock < 10:
    print(f"Stock en tension : {stock} pieces")
elif 10 <= stock:
    print(f"Stock en tension : {stock} pieces")



temperature =random.randint(1000, 2000) /100
print(temperature)

print(f"La temperature actuelle est de {temperature}°C")

temperature = 10.1 + 0.1 + 0.1
print(temperature)

print(f"La temperature actuelle est de {temperature:.2f}°C")




electricité = True

# ne pas faire d'ainterpolation de variable booléene si votre appli n'est pas en  anglais

if electricité:
    print('electricité: Vrai')
else:
    print('electricité: Faux')


print(f"le nombre tiré au hasard est : {random.randint(0, 10)}")


#@todo afficher âge partir de l'année de naissance


texte ="foo bar baz"
# len == length == longueur
print(len(texte))

print(texte.find("banane"))
print(texte.find("baz"))


print(texte.find("ba"))
# recherche à partir du caractere 5 inclus
print(texte.find("ba", 5))
print(texte.find("banana"))

texte = "Bonjour Toto"

keyword = "Toto"
# Rédiger un bloc idf qui indique si le keyword est présent ou non dans la chaine de caractéres
# afficher "trouvé" si le keyword est présent 
# sinon affichez "non trouvé" 

keyword = "Titi"
# Rédiger un bloc idf qui indique si le keyword est présent ou non dans la chaine de caractéres
# afficher "trouvé" si le keyword est présent 
# sinon affichez "non trouvé" 