brutto_cena = int(input("Podaj cenę brutto: "))
rabat = int(input("Podaj rabat w procentach: ")) / 100

vat = 0.23
netto = brutto_cena / (1 + vat)
brutto_z_rabatem = brutto_cena - brutto_cena * rabat
netto_rabat = brutto_z_rabatem / (1 + vat)

print("Cena netto to: ", netto)
print("Cena brutto po rabacie to: ", brutto_z_rabatem)
print("Cena netto po rabacie to: ", netto_rabat)
print("Podatek VAT bez rabatu: ", netto * vat)
print("Podatek VAT z rabatem: ", netto_rabat * vat)
