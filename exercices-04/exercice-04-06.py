# exo 4.6
# écrivez un bloc if qui affiche
# - "le nombre est compris entre 0 et 33 inclus" si la variable number contient une valeur comprise entre 0 et 33
# - "le nombre est compris entre 34 et 66 inclus" si la variable number contient une valeur comprise entre 34 et 66
# - "le nombre n'est pas compris entre 0 et 66 inclus" si la variable number ne contient pas de valeur comprise entre 0 et 66

import random

# affectaction d'un nombre entier entre 0 et 99 à la variable number
number = random.randint(0, 99)
print(number)

# réponse 4.6
if 0 <= number <= 33: 
    print("le nombre est compris entre 0 et 33 inclus")

elif  34 <= number <= 66:
    print("le nombre est compris entre 34 et 66 inclus" )

else:
    print("le nombre n'est pas compris entre 0 et 66 inclus")    