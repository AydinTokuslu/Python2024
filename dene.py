

while True:
    alisveris_listesi = []
    meyve = input("lütfen meyveyi giriniz, çıkmak için q'ya basınız : ")
    if meyve not in alisveris_listesi:
        alisveris_listesi.append(meyve)

    if meyve == "q":
        break
print(alisveris_listesi)