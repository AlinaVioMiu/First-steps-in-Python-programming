
# functia = o logica delimitata care poate fi refolosita
# nu ne da niciun raspuns (nu returneaza nimic)
# nu are parametri
def printGreeting():
    print('Buna ziua! Bine ati venit!')

# o f care saluta clt in functie de numele lui
# nu ne da niciun raspuns (nu returneaza nimic)
# are nevoie de parametri
def printGreetingByName(nume, prenume):
    print(f'Buna ziua {nume} {prenume}')

# o f care calculeaza media a 3 numere
# ne da un raspuns = suma nr, va avea return
# ce tip de date va avea raspunsul? 3 + 5 = 8 => int; 3 + 6 / 2 = 4.5 => double
# are nevoie de parametri
def mediaNr(a, b, c):
    return (a + b + c) / 3

# o f care ne da valoarea lui pi
# ne da un raspuns? da
# ce tip de date va avea raspunsul? => double
#are nevoie de parametri? nu
def piValue():
    return 3.14

# exercitiu: daca pers e majora true, altfel false
def verificareMajor(varsta):
    if varsta >= 18:
        return True
    else:
        return False

# zona de apelare (desktop)
printGreeting()
printGreeting()

printGreetingByName('Sinpetrean', 'Andy')
printGreetingByName('Sinpetrean', 'Crina')

print(mediaNr(3, 3, 4))

print(piValue())

print(verificareMajor(18))

# se ia varsta utilizatorului
age = int(input('Introduceti varsta dvs.'))
if verificareMajor(age): # daca e True
    print('Cont creat. Bine ati venit in aplicatie!')
else:
    print('Nu ai varsta minima necesara (18) pt a paria')

# oop
#variabile => atribute, proprietati sau fields
# functii => metode

# avand trei numere, returnati pe cel mai mare
def maxNr():
    numere = 3, 45, 5
    max_numar = max(numere)
    return max_numar
print(maxNr())