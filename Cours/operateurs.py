# +-* /*
result = 123 + 4.14
print(result)

#()
result = (1+2)*3
print(result)

# // % **
result = 1//3
print(result)

#modulo
result = 10 % 3
print(result)

#vérifie
result = 7685923 % 7
print(result)

#puissance
#dans certains langages c'est : ^, pow()
result=3**2;print(result)

#racine carré
result = 3** (1/2)
print(result)

#racine cubique
result = 3** (1/3)
print(result)

#opérateur booléan "and"
result = True and True # True
result = False and True # False
result = True and False # False

#s'il n'y a que des "and", l'ordre n'est pas important
result = True and False and True and False #False

#opérateur booléan "or
result = True or True # True
result = False or True # True
result = True or False # True
result = False or False # False

#s'il n'y a que des "or", l'ordre n'est pas important
result = True or False or True or False #True

result = not True
print(result)

result = not False
print(result)


#opérateur booléan "xor
result = True ^ True # False
result = False ^ True # True
result = True ^ False # True
result = False ^ False # False

#s'il n'y a que des "xor", l'ordre n'est pas important
result = True ^ False ^ True ^ False #True

#opérateur composés
#c++ <=> c = c +1

number = 42 
#number= number + 1
number += 1

# n'existe pas en python 
# c++ <=> c = c +1

number = 42
# number number
n = 1
number += n

# == != < > <= >=

a = 123
b = 42
result = (a == b)
print(result)

#

result = (a != b)
print(result)

#inférieur ou égale

result = (a <= b)
print(result)


# l'opérateur fait office de comparaison d'identité
a ="123"
b = 123

result = a == b
print(result)

# pas de python
#=== !==

fruits = ["apple", "banane", "cherry"]
result = "banane" in fruits 
print(result)

result = "orange" in fruits
print(result)

result = type(123) is int
print(result)

#ou

result = type(123) is float
print(result)