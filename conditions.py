import random

if True:
    print("La condition est vraie")
    print("Ce code est exécuté")

if False:
    print("La condition est fausse")
    print("Ce code n'est pas exécuté")

conditions_vente = True

if conditions_vente:
    print("L'utilisateur a accepté les conditions de vente")
else:
    print("L'utilisateur n'a pas accepté les conditions de vente")

if not conditions_vente:
    print("L'utilisateur n'a pas accepté les conditions de vente")
else:
    print("L'utilisateur a accepté les conditions de vente")

emails = random.randint(0, 3)
print(emails)

if emails == 1:
    print("Vous avez un nouveau mail")
elif emails > 1: #même chose que else if
    print(f"Vous avez {emails} nouveaux mails") #interpolation 
else:
    print("Vous n'avez pas de nouveau mail")

# TEST perso
# if emails > 0:
#     print(f"Vous avez {emails} nouveau(x) mail(s) ")
# else: 
#     print("Vous n'avez pas de nouveau mail")

windows_closed = bool(random.randint(0, 1))
electricity_off = bool(random.randint(0, 1))

print(f'{windows_closed = }')
print(f'{electricity_off = }')

if windows_closed and electricity_off:
    print("Les fenêtres sont fermées")
    print("L'électricité est coupée")
elif not windows_closed and electricity_off:
    print("Les fenêtres ne sont pas fermées")
    print("L'électricité est coupée")
elif windows_closed and not electricity_off:
    print("Les fenêtres sont fermées")
    print("L'électricité n'est pas coupée")
else:
    print("Les fenêtres ne sont pas fermées")
    print("L'électricité n'est pas coupée")

bank_card =  bool(random.randint(0, 1))
cash = bool(random.randint(0, 1))

print(f'{bank_card = }')
print(f'{cash = }')

if bank_card or cash:
    print("On a un moyen de paiement")
else:
    print("On a aucun moyen de paiement")

bank_card =  bool(random.randint(0, 1))
cash = bool(random.randint(0, 1))

print(f'{bank_card = }')
print(f'{cash = }')

if bank_card or cash:
    print("On a au moins un moyen de paiement")
    if bank_card: 
        print("On a la carte banquaire")
    if cash:
        print("On a du liquide")
else:
    print("On a aucun moyen de paiement")

ticket = bool(random.randint(0, 1))
vip = bool(random.randint(0, 1))
registration = bool(random.randint(0, 1))

print(f'{ticket = }')
print(f'{vip = }')
print(f'{registration = }')

# Quand on mélande or et and, il faut toujours utiliser les parenthèses 
if (ticket or vip) and registration:
    print("Access authorized")
else:
    print("Access not authorized")

product_count = 4

print(f'{product_count = }')

if product_count > 5 and product_count <= 20:
    print("Il y a plus de 5 articles")
    print("Il y a au moins 20 articles")
else:
    print("autre")