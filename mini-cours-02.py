# pourquoi utiliser cetaines fonctions et pas d'autres ? 

path = "/home/foo"
filename = "document.txt"

# on vérifie si le dernier caractère de path est un slash '/' ou non 
# la fonction path.endswith ('/') permet de faire le même test que path [-1] == '/':

if path.endswith ('/'):
    # le dernier caractère est un slash
    file_path = path + filename

else :
    #le dernier caractères n'est pas un slash
    file_path = path + '/' + filename

print (file_path)



# q: pourquoi est-ce que parfois in appelle une fonction dans une autre fonction ?
# r: deux critères
#   1. la lisibilité du code
#   2. optimisation du code (est-ce que j'ai besoin de réutiliser le résultat d'une fonction ?)
lenght = len(file_path)
print(lenght)

print(len(file_path))



# q: l'exo avec les nombres pair
a = 59
b = 2 
print(divmod(a, b))
print(divmod(a, b)[0])
print(divmod(a, b)[1])

# est-ce que a est divisible par b ?
print(a % b == 0)

# est-ce que a est non divisible par b ?
print(a % b != 0)



# q: l'exercice 06-09
my_list = [2.71, 42, 123, 2, 3.14, 1.61]
accumulateur = 0 

print("avant la boucle")
print(accumulateur)

print("pendant la boucle")
for item in my_list:
    accumulateur = accumulateur + item
    print(accumulateur)

print("après la boucle")    
print(accumulateur)

# q: les tableaux à 2 dimensions 

#  en python : dictionnaires dans une liste 
# en php : tableaux à index alphanumérique dans un tableau à index numérique 
# en js : des objects dans une liste  

# id    email           roles   password
# 1     foo@gmail.com   user    123
# 2     bar@gmail.com   user    123
# ... 

users = [
    [1, 'foo@example.com','admin', '123'],
    [2, 'bar@gmail.com', 'user', 'abc'],
    [3, 'baz@gmail.com', 'user', 'xyz'],
    #...
]

for line in users:
    for column in line:
        print(column)

    
compteur = 0 

for line in users: 
    if line[1].endswith('@gmail.com'):
        compteur += 1
print(f'{compteur = }')   


# une image : une largeur x = 320, une hauteur y = 200 

#       0 1 2 3 ... 319 <- x
# 0     a b c d ...   z
# 1     e x x x ...   x
# 2     f x 
# 3     g x 
# .     ..
# .     ..
# .     ..
# 199   hx

image = [
    [0,  127, 100, 55, 13],
    [10, 137, 110, 65, 23],
    [20, 147, 120, 75, 33],
    [30, 157, 130, 85, 43],
    [40, 167, 140, 95, 53],
]
somme = 0 
compteur = 0


for line in image :
    for column in line:
        if column <= 55:
            somme += column 
            compteur += 1 

moyenne = somme / compteur         

print(f'{somme = }')        
print (f'{compteur = }')
print (f'{moyenne = }')


# q: différence entre for line in lines et for i in range () ?

# boulce for avec range()
for i in range(0, 3):
    print(i)

# boucle foreach
for line in users:
    print(line)    

# même base que la boucle foreach
for i, line in enumerate(users):
    print(i, line)

# q: utilisation de len(list) dans range() ?    

# même base que la boulce avec range()
# note : len(users) == 3
for i in range(0, len(users)):
    print(i, users[i])

# q: exo 6-16

my_list = [2.71, 42, 123, 2, 3.14, 1.61]

# réponse 6-16
# on réutilise le principe d'inversion spécifique de python a, b = b, a

my_list[0], my_list[1] = my_list[1], my_list[0]
my_list[2], my_list[3] = my_list[3], my_list[2]
my_list[4], my_list[5] = my_list[5], my_list[4]
print(my_list)
    
for i in range(0, len(my_list), 2):
    print(i, i + 1)

# on recolle les morceaux 
for i in range(0, len(my_list), 2):
    my_list[i], my_list[i + 1] = my_list[i + 1], my_list[i]   
    print(my_list)

