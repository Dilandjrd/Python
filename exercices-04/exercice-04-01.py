# exo 4.1
# écrivez un bloc if qui affiche
# - "le nombre est égale à 1" si la variable number contient un 1
# - ""le nombre est différent de 1 si la variable number ne contient pas de 1

import random

# affectaction du nombre 0 ou 1 à la variable number
number = random.randint(0, 1)
print(number)

# réponse 4.1
if number == 1: 
    print('le nombre est égale à 1')

else : 
    print('le nombre est différent de 1')    

