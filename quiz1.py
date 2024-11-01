yas = int(input("lütfen yasınızı giriniz : "))
if yas <= 18:
    print("yas < 16")
elif yas > 18 and yas < 46:
    print("yasınız : ", yas)
else:
    print("yasınız tahmin edilemedi")