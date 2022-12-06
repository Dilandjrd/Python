# exo 2.5
# Stockez la valeur `3,1415` dans une variable nommée `number4`.
# Arrondissez la valeur en un float à zéro chiffre après la virgule et stockez le résultat dans une variable nommée `number4_rounded`.
# Affichez le résultat.
# Convertissez la variable `number4_rounded` en int et stockez le résultat dans une variable nommée `number4_int`.
# Affichez le résultat.

# réponse 2.5
number4 = 3.1415
number4_rounded = (round(number4, 0))

print(number4_rounded)

number4_rounded = int(number4_rounded)
number4_int = number4_rounded

print(number4_int)

