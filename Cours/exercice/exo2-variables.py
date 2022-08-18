# exercice-02-variables.py

# exo 2.1
# Affectez :
# - le nombre 42 à une variable
# - le nombre d'or 1,61 à une variable
# - votre nom et prénom à une variable
# - la valeur booléenne vrai si nous sommes le matin, sinon la valeur booléenne faux, à une variable
# - la valeur nulle `None` à une variable
# Affichez ces variables

# réponse 2.1

nombre = 42
print(nombre)

nombre_or = 1.61
print(nombre_or)

nickname_lastname = "Monkey D Hugo"
print(nickname_lastname)

is_morning = True
print(is_morning)

is_not_morning = False
print(is_not_morning)

null = None
print(null)

# code 2.1
# la fonction `round()` permet d'arrondir un float en un integer
# 0,1 est arrondi à la valeur inférieur
print(round(0.1))
# 0,9 est arrondi à la valeur supérieur
print(round(0.9))
# la fonction `round()` permet aussi d'arrondir en précisant le nombre de chiffres après la virgule
# arrondir à un nombre décimal à 4 chiffres après la virgule
print(round(1 / 3, 4))

# exo 2.2
# Stockez les valeurs suivantes dans une variable et transtypez-les :
# - integer 2 en un float
# - float 1,62 en un integer
# - float 1,62 en un float arrondi à zéro chiffre après la virgule, puis en un integer
# - float 1,62 en un float arrondi à un chiffre après la virgule
# À chaque fois stockez le résultat dans une variable et affichez le résultat.

# réponse 2.2
number1 = 2
print(int(number1))

number2 = 1.62 
print(float(number2))

number3= 1.62
number4 = (int(round(number3)))
print(int(number4))

number5 = 1.62
print(round(number5,1))