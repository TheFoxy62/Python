#import random

# Vérification de Fruits.#

# fruits = ['apples','bananas', 'cherries']
# if 'apples' in fruits:
#      print("Il y a des pommes")
#  else:
#      print("IL n'y a pas de pommes")

#  if 'Oranges' in fruits:
#      print("il y a des Oranges")
#  else:
#      print("Il n'y a pas Oranges")


## Authentification ##

# Authenticated d'un Utilisateur d'unne page Web.#
#  is_authenticated = True

#  if is_authenticated:
#      print("L'Utilisateur peut accéder aux backoffice")
#  else:
#     print("L'Utilisateur ne peut pas accéder aux backoffice")

#  is_authenticated = False
#  if is_authenticated:
#     print("L'Utilisateur ne peut pas accéder aux backoffice")
#  else:
#     print("L'Utilisateur peut accéder aux backoffice")



## La forme du Login/Mot de passe. ##

# user_password = "123"
# user_password_in_db = "abc"
# if user_password == user_password_in_db:
#     print("L'Utilisateur peut accéder aux backoffice")
# else:
#     print("Login ou le mot de passe est incorrect")

# user_in_db= ['toto', 'titi','tata', 'tutu']
# tutu_password_in_db = "abc"

# user_name_in_form = 'tutu'
# user_password_in_form = "123"

# if Nom d'utilisateur verifie la liste des nom + la forme du mot de passe + le mot de passe.

# if user_name_in_form in user_in_db and user_password_in_form == tutu_password_in_db:
#     print("L'Utilisateur peut accéder aux backoffice")
# else:
#     print("L'Utilisateur ne peut pas accéder aux backoffice")

# #Login/mot de passe remplacer par User_name_in_form est user_password_in_form par True.

# user_password = "123"
# user_password_in_db = "abc"
# if user_password == user_password_in_db:
#     print("L'Utilisateur peut accéder aux backoffice")
# else:
#     print("Login ou le mot de passe est incorrect")

# user_in_db= ['toto', 'titi','tata', 'tutu']
# tutu_password_in_db = "abc"

# user_name_in_form = 'tutu'
# user_password_in_form = "abc"

# if True :
#     print("L'Utilisateur peut accéder aux backoffice")
# else:
#     print("L'Utilisateur ne peut pas accéder aux backoffice")


# #la valeur de authenticated est vraie, mais il faut que le login est le mot de passe soit correct. 

# is_authenticated = True

# user_in_db = ['toto', 'titi','tata', 'tutu']
# tutu_password_in_db = "abc"

# user_name_in_form = 'tutu'
# user_password_in_form = "123"

#if is_authenticated or user_name_in_form in user_in_db and user_password_in_form == tutu_password_in_db:
 #   print("L'Utilisateur peut accéder aux backoffice") Exemple!: if true / if False de la valeur de l'authenticated 
#else:
 #   print("L'Utilisateur ne peut pas accéder aux backoffice")

#-----------

#if False:
 #       print("L'Utilisateur peut accéder aux backoffice")
#else:
  #  print("L'Utilisateur ne peut pas accéder aux backoffice")

# or 

#if True:
#    print("L'Utilisateur peut accéder aux backoffice")
#else:
 #   print("L'Utilisateur ne peut pas accéder aux backoffice")




#2.0 

# /electricity = bool(random.randint(0,1))
#water = bool(random.randint(0,1))
#gas = bool(random.randint(0,1))

#2.1 

# /vérifier que toutes les sources sont coupées
#si c'est la cas , affichez le message "Vous pouvez partie en we"
#Sinon, affichez le message "Il reste des sources à couper"

# electricity_is_off = bool(random.randint(0,1))
# water_is_off= bool(random.randint(0,1))
# gas_is_off= bool(random.randint(0,1))

# print('electricity_is_off:',electricity_is_off)
# print('water_is_off:', water_is_off)
# print('gas_is_off:', gas_is_off)

# if electricity_is_off and water_is_off and gas_is_off:
#     print("Vous pouvez partir en we")
# else:
#     print("Il reste des sources à couper")

# # or 

# electricity_is_on = bool(random.randint(0,1))
# water_is_on= bool(random.randint(0,1))
# gas_is_on= bool(random.randint(0,1))

# print('electricity_is_on:',electricity_is_on)
# print('water_is_on:', water_is_on)
# print('gas_is_on:', gas_is_on)

#if electricity_is_on and water_is_on and gas_is_on:
  #   print("Vous pouvez partir en we")
#else:
  #   print("Il reste des sources à couper")

# if not electricity_is_on and not water_is_on and not gas_is_on:
#     print("Vous pouvez partir en we")
# else:
#     print("Il reste des sources à couper")


#Exemple#

#foo = True
#print(foo)
#----
#print(foo = True) ou print(True) ou print(False)  

# if not electricity_is_off:
#     print("Couper l'electricité")

# if not water_is_off:
#     print("Couper l'eau")

# if not gas_is_off:
#     print("couper le gaz")

# or 

# if not electricity_is_on:
#     print("Ne pas couper l'electricité")

# if not water_is_on:
#     print("Ne pas couper l'eau")

# if not gas_is_on:
#     print("Ne pas couperle gaz")



##CASH/CARD/CHECK##

# has_cash = bool(random.randint(0,1))
# has_card = bool(random.randint(0,1))
# has_check= bool(random.randint(0,1))


#Vérifier qu'au moins un moyen de paiement est disponible
#si c'est le cas, affichez le message "Vous pouvez partir" faire les course"
#sinon, affichez le message "Vous n'avez aucun moyen de paiement"

# has_cash_is_off = bool(random.randint(0,1))
# has_card_is_off = bool(random.randint(0,1))
# has_check_is_off= bool(random.randint(0,1))


# print('has_cash_is_off',has_cash_is_off)
# print('has_card_is_off',has_card_is_off)
# print('has_check_is_off',has_check_is_off)


# if has_cash_is_off or has_card_is_off or has_check_is_off:
#  print("vous pouvez payer")
# else:
#  print("vous avez pas de quoi payer")


#or 

# has_cash_is_on = bool(random.randint(0,1))
# has_card_is_on = bool(random.randint(0,1))
# has_check_is_on= bool(random.randint(0,1))

# print('has_cash_is_on',has_cash_is_on)
# print('has_card_is_on',has_card_is_on)
# print('has_check_is_on',has_check_is_on)


# if has_cash_is_on or has_card_is_on or has_check_is_on:
#  print("vous pouvez payer")
# else:
#  print("vous avez pas de quoi payer")


# Age #

# age =random.randint(0, 100)

#0-5 bebe
#6-11 enfant
#12-25 ado - jeune adulte
#26-59 adulte
#60+ senior

# if age <= 5:
#     print('bébé')
# elif 6 <= age <= 11:
#     print('enfant')
# elif 12 <= age <= 25:
#     print('ado, jeune adulte')
# elif 26 <= age <= 59:
#     print('ado, jeune adulte')

# on peut aussi faire un else pour intercepter les cas ou l'age >= 60

# elif age >= 60:
#     print('senior')


# Bool #

# if bool(123):
    # le message s'affichera car bool(123) == True
#     print('Il y a une valeur numérique')

# if bool(0):
    # le message ne s'affichera pas car bool(0) == False
    # print("Il y a une valeur nulle")