# exo 4.5
# écrivez un bloc if qui affiche
# - "le nombre est compris entre 0 et 49 inclus" si la variable number contient une valeur comprise entre 0 et 49
# - "le nombre n'est pas compris entre 0 et 49 inclus" si la variable number ne contient pas de valeur comprise entre 0 et 49

import random

# affectaction d'un nombre entier entre 0 et 99 à la variable number
number = random.randint(0, 99)
print(number)

# réponse 4.5
if  0 <= number <= 49:
    print("le nombre est compris entre 0 et 49 inclus")

else : 
    print("le nombre n'est pas compris entre 0 et 49 inclus")




