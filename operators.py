import random
import math

# = affectation
foo = 123 

# + addition
foo = 123 + 42 
foo = foo + 42 
# += opérateur d'incrémentation
foo += 42 
print(foo)

# foo++ équivalent de foo += 1
# mais l'opérateur ++ n'éxiste pas en python

# - soustraction
foo = 123 - 42
foo = foo - 42
# -= opérateur de décrémentation 
foo -= 42
print(foo)
 
 # foo-- équivalent de foo -= 1 
 # mais l'opérateur -- n'éxiste pas en python

# / divison 
foo = 123 / 42 
foo /= 42 
print(foo)
print(type(foo))

# // division entière 
foo = 123 // 42
foo //= 42 
print(foo)
print(type(foo))

# % modulo
foo = 4 % 3
foo = random.randint(1, 100)
print(foo)
print(foo % 2)
foo %= 2 

# * multiplication


# ** puissance
foo = 2 ** 2 
foo = 2 ** 3 
print(foo)

# ^ puissance mais pas en python 

# math.sqrt () racine carré
# ** 0.5 racine carré
foo = math.sqrt(4)

# 0.5 == 1/2
foo = 4 ** 0.5
foo = 4 ** (1/2)
# racine cubique
foo = 8 ** (1/3)
print(foo)

# les opérateurs de comparaison 

# l'égalité ==
result = 1 == 1 
print(result)
# à ne pas confondre avec l'affectation =
# à ne pas confondre avec l'identité === (qui n'éxiste pas en python)

# les grandeurs
# plus petit que
result = 123 < 42 
print(result)

# plus grand que 
result = 123 > 42
print(result)

# plus grand ou égal à 
result = 123 >= 42
print(result)

# l'inégalité (ou différence)
result = 123 != 42
print(result)

# les encadrements 
# <> <= >=
my_number = random.randint(0, 100)
print(my_number)
result = 0 <= my_number <= 50
print(result)

# operateur and (et)
result = True and False
print(result)
result = False and True
print(result)
result = True and True
print(result)
result = False and False
print(result)

a =random.randint(0, 1)
b = random.randint(0, 1)
result = bool(a) and bool(b)
print(a, b)
print(result)

# utilisations un peu spéciales des comparaisons de grandeur
result = "abc" > "bcd" # une lettre a un chiffre définie par rapport au ascii (voir sur internet)
print(result)

# operateur or (ou)
result = True or False
print(result)
result = False or True
print(result)
result = True or True
print(result)
result = False or False
print(result)

# opérateur not (négation)
result = not True
print(result)
result = not False
print(result)

fruits = ['abricot', 'baies', 'cerise']
result = 'ananas' in fruits
print(result)
result = 'cerise' in fruits
print(result)

