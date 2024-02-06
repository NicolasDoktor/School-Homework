cena_kebabu = [2,3,4]
vzdalenost = [7,3,5]

cena_jizdenky = 4

vysledne_ceny = []

for i in range(len(cena_kebabu)):
    suma = cena_kebabu[i] + (cena_jizdenky*vzdalenost[i])
    vysledne_ceny.append(suma)

print(min(vysledne_ceny))
#vypíše nejmenší útratu za kebab a jízdu
