# if True:
#     print('ce message sera toujours affiché')

#les type de boucle:
# - while
# - do while
# - for classique
# - for each


#reproduction d'une boucle for classique avec une boucle while
# condition d'initialisation 

import random


counter = 0
# la taille de la boucle 
limit = 10

# while True:

while counter < limit:

    # condition d'arret 
    # if counter >= limit:
    #     break
    # print("je boucle!!!!")

    # action à répéter
    print("tour:", counter)

    # incrément / décrement 
    counter += 1 

# reproduction d'une boucle do while avec une boucle while
counter = 0
# taille de la boucle
limit = 10 

while True:
    # action à répeter
    print("do while", counter)

    # incrément / décrement 
    counter += 1 

    # condition de continuation
    if not (counter < limit):
        break

# for de python

for counter in range(0, 10):
    #action à répéter
    print('for python', counter)

# for de python
mots = ['foo','bar','baz']

# Méthode non recommandé pour boucler sur tous les éléments d'une liste
for i in range(0, len(mots)):
    #action à répéter
    print(f"mot (reco) {i}:", mots[i])


# Méthode recommande pour boucler sur tous les elements d'une liste
for mot in mots:
    #action à répéter
    print("mot (reco", mot)

for mot in enumerate(mots):
    # action à répéter
    print(f"mot (reco) {i}:", mot)

# exo1: affichez les nombres de 100 à 999 avec une boucle for
# réponse
for counter in range(100, 1000, 1):
    print('for exo1:', counter)

# exo2: affichez les nombres de 0 à 20 sont multiples de 3
#réponse
start= 0
end= 20
step= 3
for i in range(0, 20+1 , 3):
    print(i) 

# exo3: afffichez les nombres de 10 à 1 rebours
#réponse
for i in range(-10,0,1):
    print(i)

# info : la fonction range() prend un troisiéme parametre qui indique le "pas" (step)




# algo: tirage de  3 nombres différents parmi 5
numbers = []

#1éme tirage
n = random.randint(1, 5)
numbers.append(n)

#2éme, 3eme et 4 eme tirage
for i in range(0, 3):
   while True:
      n = random.randint(1, 5)

# conditions d'arret
      if n not in numbers:
          # le nombre n'a pas encore été tiré au hasard
          # on peut sortir de la boucle
          break

   numbers.append(n)

print(numbers)