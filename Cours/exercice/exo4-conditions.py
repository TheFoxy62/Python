# exercice-04-conditions.py

import random

# code 4.1
# la fonction `random.randint()` permet de tirer un nombre entier au hasard
# affectaction d'un nombre entier entre 0 et 99 à la variable number
number = random.randint(0, 99)
print(number)

# exo 4.1
# écrivez un bloc if qui affiche
# - "le nombre est égale à 1" si la variable number contient un 1
# - "le nombre est différent de 1" si la variable number ne contient pas de 1

# affectaction du nombre 0 ou 1 à la variable number
number = random.randint(0, 1)
print(number)

# réponse 4.1
if number == 1:
    print("le nombre est égale à 1")
else:
    print("le nombre est différent de 1")

# code 4.2
# si 10 est un nombre pair, le modulo de 2 est égal à zéro
print(10 % 2)
# si 21 est un nombre impair, le modulo de 2 n'est pas égal à zéro (il est égal à 1)
print(21 % 2)

# exo 4.2
# écrivez un bloc if qui affiche
# - "le nombre est pair" si le modulo par 2 de la variable number est égal à zéro
# - "le nombre est impair" si le modulo par 2 de la variable number n'est pas égal à zéro

# affectaction d'un nombre entier entre 0 et 9 à la variable number
number = random.randint(0, 9)
print(number)

# réponse 4.2

if (number % 2) == 0:
    print("le chiffre est pair")
else:
    print("le chiffre est impair")

print("\n")

# exo 4.3
# Écrivez un bloc if qui affiche
# - "le nombre est divisible par 3" si la variable number est divisible par 3
# - "le nombre n'est pas divisible par 3" sinon

# affectaction d'un nombre entier entre 0 et 9 à la variable number
number = random.randint(0, 9)
print(number)

# réponse 4.3

if number % 3:
    print("le chiffre n'est pas divisible par 3")
else:
    print("le chiffre est divisible par 3")
print("\n")

# exo 4.4
# écrivez un bloc if qui affiche
# - "le nombre est supérieur ou égale à 5" si la variable number contient une valeur plus grande ou égale à 5
# - "le nombre est inférieur à 5" si la variable number ne contient pas de valeur plus grande ou égale à 5

# affectaction d'un nombre entier entre 0 et 9 à la variable number
number = random.randint(0, 9)
print(number)

# réponse 4.4
if number >= 5:
    print("le chiffre est supérieur a 5")
else:
    print("le chiffre est inférieur a 5")
print("\n")

# exo 4.5
# écrivez un bloc if qui affiche
# - "le nombre est compris entre 0 et 49 inclus" si la variable number contient une valeur comprise entre 0 et 49
# - "le nombre n'est pas compris entre 0 et 49 inclus" si la variable number ne contient pas de valeur comprise entre 0 et 49

# affectaction d'un nombre entier entre 0 et 99 à la variable number
number = random.randint(0, 99)
print(number)

# réponse 4.5
if number <= 49:
    print("le nombre est compris entre 0 et 49 inclus")
else: 
    print("le nombre n'est pas compris entre 0 et 49 inclus")
print("\n")

# exo 4.6
# écrivez un bloc if qui affiche
# - "le nombre est compris entre 0 et 33 inclus" si la variable number contient une valeur comprise entre 0 et 33
# - "le nombre est compris entre 34 et 66 inclus" si la variable number contient une valeur comprise entre 34 et 66
# - "le nombre n'est pas compris entre 0 et 66 inclus" si la variable number ne contient pas de valeur comprise entre 0 et 66

# affectaction d'un nombre entier entre 0 et 99 à la variable number
number = random.randint(0, 99)
print(number)

# réponse 4.6
if number <= 33:
    print("le nombre est compris entre 0 et 33 inclus")
elif number <= 34 >= 66:
    print("le nombre est compris entre 34 et 66 inclus")
elif number >= 66:
    print("le nombre n'est pas compris entre 0 et 66 inclus")
print("\n")

# exo 4.7
# écrivez un bloc if qui affiche
# - "le nombre a est supérieur au nombre b" si la variable a contient une valeur plus grande que celle de la variable b
# - "le nombre a est inférieur au nombre b" si la variable a contient une valeur plus petite que celle de la variable b
# - "les deux nombres a et b sont égaux" si les deux variables a et b contiennent la même valeur

# affectaction d'un nombre entier entre 0 et 99 à la variable a
a = random.randint(0, 99)
print(a)

# affectaction d'un nombre entier entre 0 et 99 à la variable b
b = random.randint(0, 99)
print(b)

# réponse 4.7
if b < a :
    print("le nombre a est supérieur au nombre b")
elif b > a:
    print("le nombre a est inférieur au nombre b")
elif a == b:
    print("les deux nombres a et b sont égaux")
print("\n")

# code 4.3
# affichage d'une variable avec une f-string
number = 42
print(f"number : {number}")

# exo 4.8
# De nouveaux messages sont arrivés dans la boîte mail.
# Vous voulez afficher une notification à l'utilisateur.
# Mais il faut respecter les règles de français.
# Affichez le message :
# - "il n'y a aucun mail" si le nombre de nouveaux mails est égal à 0
# - "il y un nouveau mail" si le nombre de nouveaux mails est égal à 1
# - "il y a X nouveaux mails" (où X représente le nombre de nouveaux mails) si le nombre de nouveaux mails est supérieur à 1
# Utilisez une f-string pour le dernier message

# affectaction d'un nombre entier entre 0 et 5 à la variable mails
mails = random.randint(0, 5)
print(mails)

# réponse 4.8
if mails == 0:
    print("il n'y a aucun mail")
elif mails == 1:
    print("il y un nouveau mail")
elif mails >=2:
    print("il y a "f"{mails} ""nouveaux mails")