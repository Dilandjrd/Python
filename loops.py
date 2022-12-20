while False:
    print('ce message ne sera pas affiché')

# warning boucle infini
# while True:
 #  print('ce message sera affiché en boucle')
    
counter = 10 

#while counter:
    #print(f"{counter = }")
    #counter -= 1
    # même chose
    # counter = counter -1

counter = 0
# le nombre de boucle == valeur limite - la première valeur du compteur
while counter <= 10:
    print(f"{counter = }")
    counter += 3
    # même chose
    # counter = counter + 1

# boucle de type for == pour
for counter in range(0, 10):
    print(f'{counter =}')   

# le 3ème paramètre de range permet de spécifier l'incrément
# exemple avec un incrément de 2 (au lieu de 1) 
for counter in range (0, 10, 2):  
    print(f'{counter=}')  

# compte à rebours
for counter in range(10, 0,-1):
    print(f'{counter}')

fruits = ['abricot', 'baies', 'cerise']

# boucle de type for each == pour chaque
for fruit in fruits:
    print(fruit)

# boucle de type for each == pour chaque
# avec index
for i, fruit in enumerate (fruits):
    print(f'{i + 1}: {fruit}') 

for i in range(0, len(fruits), 3):
    print(fruits[i])



# reversed () renvoie un itérateur économe en mémoire
print (reversed (fruits)) 
# [::1] renvoie une liste dont la taille est égale à la liste originale (peut ne pas être économe en mémoire)
print (fruits[::-1])  

for fruit in reversed(fruits):
    print(fruit)

for fruit in fruits[::-1]:
    print (fruit)

my_list= [123, 2, 42, 3.14, 2, 56, 2]
my_number = 2
counter = 0

for item in my_list: 
    if item == my_number:
        counter += 1 
        #print(item)

print(f'{counter =}')

accumulateur = 0 

for item in my_list:
    accumulateur += item

print(f'{accumulateur}')


my_array = [
    ['a','c'],
    ['b','d']
] 

# une boucle for dans une boucle for 
# len (my_array) me donne le nombres de lignes
for i in range(0,len (my_array)):

# len (my_array[0]) me donne le nombre de colonne
    for j in range(0, len(my_array[0])):
        print(i, j, my_array[i][j])




