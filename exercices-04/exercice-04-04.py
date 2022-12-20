# exo 4.4
# écrivez un bloc if qui affiche
# - "le nombre est supérieur ou égale à 5" si la variable number contient une valeur plus grande ou égale à 5
# - "le nombre est inférieur à 5" si la variable number ne contient pas de valeur plus grande ou égale à 5

import random

# affectaction d'un nombre entier entre 0 et 9 à la variable number
number = random.randint(0, 9)
print(number)

# réponse 4.4
if number >= 5 : 
    print("le nombre est supérieur ou égale à 5")

else : 
    print("le nombre est inférieur à 5")    
