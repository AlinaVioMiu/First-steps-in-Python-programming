'''
Operatori:
 -de atribuire: =
- aritmetici: +,-,/, *, % (modulo = restul impartirii)
- de comparare: <, >, ==, !=(diferit), <=, >=
- logici: and, or, ! (not = pui o intrebare si intorci rezultatul)
'''

a = 3
b = 5
print(a+b) # 3+5 => 8
print(a==b) # a=b => False
print( a<4 and a<4) # True si True => True
print( a<4 or a<2) # True SAU False => True

# cu mama sau tata sau (cu bunicu si bunica)
mama = True
tata = False
bunicu = False
Bunica = False
print(mama or tata or (bunicu and bunica)) # True