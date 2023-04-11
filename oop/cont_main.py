from oop.cont_bancar import ContBancar

cont1 = ContBancar('Andy S', 'RO001')
cont2 = ContBancar('Crina S', 'RO002')

cont1.activareCont(7777)
cont2.activareCont(3333)
cont2.activareCont(7777)

cont1.alimentareCont(300)
cont2.alimentareCont(700)
cont2.alimentareCont(300)

cont1.platacard(300)
cont2.platacard(400)
cont2.platacard(400)

cont1.interogareSold()
cont2.interogareSold()
# tema
# clasa angajat
#nume, prenume, salariu, vechime, functie
#constructor: nume, prenume, salariu, vechime, functie
# metode
# descriere
# actualizare vechime (parametru noua vechime)
    # self,vechime = noua_vechime
# marire salariu in functie de vechime: < 5 ani marire cu 300, > 5 ani = marire cu 500

