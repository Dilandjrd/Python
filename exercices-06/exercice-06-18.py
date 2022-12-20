# exo 6.18
# Avec le même tableau en 2 dimensions, affichez toutes les valeurs plus petites ou égales à 50 ainsi que leur cordoonnées (ligne et colonne)
# Vous pouvez réutiliser la variable `size` qui a permis de construire le tableau en 2 dimensions
#
# ATTENTION : cet exercice nécessite l'utilisation d'une boucle `for`

import random

size = 5
matrix = []

for _ in range(0, size):
    row = [random.randint(40, 100) for _ in range(0, size)]
    matrix.append(row)

print(matrix)

# réponse 6.18

