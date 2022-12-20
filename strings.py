my_text1 = """Texte
multi-ligne
abc
foo
bar"""

print(my_text1)

my_text2 = "Texte\nmultti-ligne\nabc\nfoo\bar"

print(my_text2)

my_number1 = 123

my_text3 = f"Nombre = {my_number1}"

print(my_text3)

my_text4 = f"""
Le nombre
est
{my_number1}
foo"""

print(my_text4)

my_nnumber2 = 3.14
my_text5 = "Le nombre PI est " + str(my_nnumber2) + "\nEt le nombre d'or est 1.618"
print(my_text5)

# Tronquer un float dans une interpolation

my_nnumber3 = 1 / 3
my_text6 = f"1 / 3 ~= {my_nnumber3:.4f}"
print(my_text6)

my_text7 = f"1+1= {1+1}"
print(my_text7)

# Définition d'une fonction utilisateur 
# l'écriture de documentation pour une fonction
def hello(name: str) -> None:
    """Cette fonction dit bonjour à quelqu'un
    name str indique le nom de la personne à saluer 
    return None
    """
    print(f"Salut {name}")

# Appel d'une fonction 
hello("Toto")

help(hello)

my_text8 = "Lorem ipsum, dolor sit amet consectetur adipisicing elit. Molestiae officiis facilis doloremque veritatis ipsum architecto earum distinctio doloribus, similique tempore nulla eligendi dolore et neque magni in aperiam assumenda necessitatibus temporibus!"
# longueur d'une str
my_number4 = len(my_text8)
print(my_number4)

# trouver la position d'une str dans une autre str
my_number5 = my_text8.find('dolor')
print(my_number5)

my_number5 = my_text8.find('ipsum' , my_number5 + 1)
print(my_number5)

# Compte le nombre d'occurence d'ne str dans une autre str
my_number6 = my_text8.count('l')
print(my_number6)

# non permanent
print(my_text8.replace("Lorem" , "foo")) # affiche le texte avec modification
print(my_text8) # text d'origine

# permanent
my_text8 = my_text8.replace("Lorem" , "foo")
print(my_text8) # text modifié 

my_list1 = my_text8.split()
print(my_list1)
print(len(my_list1))

# accès en lecture a un caractère de la str

print(my_text8[0])

# accès en lecture a un caractère de la str (du 0 au 10eme)

print(my_text8[0 : 10])

# accès en lecture a un caractère de la str (du 10eme jusqu'à la fin)

print(my_text8[10 :])

# accès en lecture par la fin

print(my_text8[ ::-1])

# accès en lecture 1 caractères sur 2

print(my_text8[ :: 2])