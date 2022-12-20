# exo 4.3
# Écrivez un bloc if qui affiche
# - "le nombre est divisible par 3" si la variable number est divisible par 3
# - "le nombre n'est pas divisible par 3" sinon

import random

# affectaction d'un nombre entier entre 0 et 9 à la variable number
number = random.randint(0, 9)
print(number)

# réponse 4.3
if number % 3 == 0 :
    print("le nombre est divisible par 3")

else :
    print ("le nombre n'est pas divisible par 3")   

