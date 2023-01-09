# scope ou la portée des variables 
# le scope fonctionne exactement de la même maniére en JS

foo = 123 # scope global

def bar ():
    foo = 42 # scope local
    print(foo)

print(foo) #123, scope global
bar() #42 , scope local de la fonction bar()
print(foo) #123, scope global

def baz():
    print('baz', foo) # scope global
    lorem = 'ipsum'

baz() #123, scope global
# print(lorem) # l'appel est dans le scope mais la variable lorem est dans un scope local
    