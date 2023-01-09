from collections.abc import Callable
# import my_library                 # Pour importer la libraire en entière 
from my_library import randint_list # Récupère juste la fonctionrandint_list dans la librairie 

def addition(a: float, b: float) -> float: 
    """Cette fonction permet d'additionner deux nombre

    a float le preimier nombre à additionner 
    b float le deuxième nombre à additionner
    return float le résultat de l'addition 
    """
    result = a + b 

    return result

result = addition(123, 42)
print(result)

my_number1 = 123 
my_number2 = 42 
result = addition(my_number1, my_number2)
print(result)

def calculer(calcul1: Callable, calcul2:
Callable, a: float, b: float, c: float) -> float:    
    result = calcul1(a, b)
    result = calcul2(result, c) 

    return result

result = calculer(addition, addition, 123, 42, 3.14)
print(result)

my_list = randint_list(0, 100, 10)
print(my_list)

my_list = randint_list(0, 10, 300)
print(my_list)    


# écrire une liste qui accepte en paramètre une liste et qui renvoie la moyenne des nombres de la liste

def my_average(numbers: list) -> float:
    my_sum = 0 

    for number in numbers:
        my_sum+= number

    result = my_sum / len(numbers)    

    return result 





