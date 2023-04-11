class AngajatCompanie:
    def __init__(self, nume, prenume, salariu, functie, vechime):
        self.nume = nume
        self.prenume = prenume
        self.salariu = salariu
        self.functie = functie
        self.vechime = vechime
    #descriere
    def descriere_angajat(self):
            print(f'Nume complet angajat: {self.nume} {self.prenume}')
            print(f'Salariu {self.salariu}')
            print(f'Functie {self.functie}')
            print(f'Vechime {self.vechime} ani')
            print(f'---------------------')
    #actualizare vechime
    def actualizare_vechime(self, noua_vechime):
            self.vechime = noua_vechime
            print(f'Noua vechime a angajatului {self.nume} {self.prenume} este de {self.vechime} ani')
            print(f'---------------------')
    #marire salariu
    def marire_salariu(self, vechime):
        if vechime < 5:
            print(f'Angajatul {self.nume} {self.prenume} beneficiaza de o marire salariala de 300 lei')
            self.salariu = self.salariu + 300
            print(f'Noul salariu este de {self.salariu}')
        elif vechime >= 5:
            print(f'Angajatul {self.nume} {self.prenume} beneficiaza de o marire salariala de 500 lei')
            self.salariu = self.salariu + 500
            print(f'Noul salariu este de {self.salariu}')
        else:
            print(f'Angajatul {self.nume} {self.prenume} nu beneficiaza de marire salariala')
        print(f'---------------------')




