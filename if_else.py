# CTRL + / => sa comentam mai multe linii
piesa_faina = True
# if
print('pornim radio')
if piesa_faina == True:
    print('dam mai tare')
    print('incep sa fredonez piesa')
print('oprim radio')

# if else
# daca numarul este par printam acest lucru
# altfel printam impar
nr = 4
# ce inseamna par? se imparte exact la 2
# ce inseamna ca se imparte la 2? ne da rest 0
if nr % 2 == 0: # daca restul impartirii numarului la 2 este 0
    print('numar par')
else:
    print('numar impar')

# este numarul pozitiv?
if nr > 0:
    print('numar pozitiv')
else:
    print('numarul nu este pozitiv')
# daca utilizatorul are sub 18 ani, nu poate paria altfel poate
varsta = int(input('introdu varsta'))
if varsta < 18:
    print ('Varsta mai mica de 18 ani. Nu poti paria')
else:
    print('Poti paria')

# if, else if, else
# cum ne saluta robotelul in functie de ora?

# luam date de la tastatura
# ne asiguram ca sunt transformate din str in int
ora = int(input('Introdu ora'))
if ora < 0:
    print('ora negativa')
elif ora <= 11:
    print('buna dimineata')
elif ora <= 18:
    print('buna ziua')
elif ora <= 21:
    print('buna seara')
elif ora <= 24:
    print('noapte buna')
else:
    print('ora mai mare decat 24')
# CTRL + / => sa comentam mai multe linii

# robot telefonic
optiune = int(input('Alege o optiune'))
if optiune == 0:
    print('revenire meniu anterior')
elif optiune == 1:
    print('ati ales RO')
elif optiune == 2:
    print('ati ales EN')
else:
    print('nu am identificat optiunea, mai incearca')