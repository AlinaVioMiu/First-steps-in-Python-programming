# variabila = zona din memoria calc care tine date
# variabila = cutie in care punem valori

# am declarat (i-am dat un nume) si initializat variabila MARCA
# nu putem sa punem spatiu in numele variabilei
# o variabila incepe cu litera mica
marca_masina = 'Volvo'
model_masina = 'XC60'
# loosly typed = nu treb sa specificam tipul de date

print(f'Am cumparat o masina marca: {marca_masina}')
print(f'Este modelul: {model_masina}')

# suprascriere (overwrite)
model_masina = 'XC60 facelift'
print(f'Am cumparat o masina marca: {marca_masina}')
print(f'Este modelul: {model_masina}')

nume = 'Sinpetrean'
prenume = 'Andy'
varsta = 34
print(prenume + ' ' + nume )
print(f'{prenume} {nume} are varsta de {varsta}')

for i in range (1, 20, 3):
    print(i)
