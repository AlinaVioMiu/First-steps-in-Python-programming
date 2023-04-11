# while = loop, ciclu repetitiv, nu stim cate repetari vor fi
# problema: masina merge cat tp inca are benzina

litri_benzina = 10
while litri_benzina > 0:
    # acceleram
    print('vruum, vruum')
    # scadem benzina
    litri_benzina = litri_benzina - 1
    if litri_benzina <= 3:
        print('se aprinde becul rosu!')
print('stop!')
