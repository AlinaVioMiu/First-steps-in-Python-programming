'''
for => loop, structura repetitiva (stim cate repetari vrem sa facem) ce rasp la:
de unde incepem?
pana unde mergem
pasul de parcurgere
'''
# problema: printam 101 dalmatieni
# for i in range (1, 102):
#      print(f'Dalmatianul cu nr {i}') # f inseamna format string

# # problema: printam 101 dalmatieni din 2 in 2
# for i in range (1, 102, 2): # nu vedem 102 pt ca index incepe de la 0
#     print(f'Dalmatianul cu nr {i}')

# parcurgere lista cu for prin intermediul indexului
#numere = [3, 7, 10, 20, 30]
# for i in range(0, len(numere)):
#     print(f'indexul curent este {i}')
#     print(f'numarul curent este {numere[i]}')

# for each = parcurge toate elementele din array si ajunge direct la valoare
# for numar in numere:
#     print(f'numarul curent este {numar}')

# algoritm cu suma numerelor
# s = 0
# for numar in numere:
#     print(f'numarul curent este {numar}')
#     s = s + numar
# print(f'Suma este {s}')

# TEMA: de cate ori apare 3 [3, 2, 3, 5, 3, 3]
lista_numere = [3, 2, 3, 5, 3, 3, 3]
# for i in range(0, len(lista_numere)):
#     print(f'numarul curent este {lista_numere[i]}')
# print(lista_numere.count(3))
print(f'numarul 3 apare de {lista_numere.count(3)} ori')