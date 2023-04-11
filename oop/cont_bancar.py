class ContBancar:
    # oop = object oriented programming
    # contructor = are rolul de a impune date de start
    def __init__(self, titularCont, iban):
    # propietati, atribute, fields
        self.titularCont = titularCont
        self.iban = iban
        self.sold = 0
        self.activ = False
        self.pin = 7777
        self.incercari_activare = 0

    # metode
    def salut(self):
        print(f'Buna {self.titularCont}')

    def interogareSold(self):
        self.salut()
        print(f'IBAN {self.iban}')
        print(f'Sold {self.sold}')
        print(f'Activ {self.activ}')
        print(f'Numar de incercari {self.incercari_activare}')
        print(f'---------------------')

    def activareCont (self, pin_utilizator):
        self.salut()
        if pin_utilizator == self.pin:
            print(f'Card activat cu succes')
            self.activ = True
        else:
            print(f'PIN gresit')
            self.incercari_activare = self.incercari_activare + 1
            # self.incercari_activare+=1 , e varianta prescurtata

    def alimentareCont (self, suma):
        self.salut()
        self.sold += suma
        print(f'Ati alimentat cu suma {suma}')
        print(f'Aveti in cont {self.sold}')

    def platacard (self, suma):
        self.salut()
        #pot sa cheltuiesc doar ce am
        #daca suma este <= decat sold
        if suma <= self.sold:
            self.sold -= suma
            print(f'Ati cheltuit suma {suma}')
            print(f'Aveti in cont {self.sold}')
        else:
            print(f'Fonduri insuficiente')











