from random import randint


def sayiTahmin():
    oyunDurumu = True
    while oyunDurumu:
        rastgeleSayi = randint(1, 20)
        hak = 5
        print("Sayı tahmin oyununda {} hakkınız vardır, iyi kullanın!!!".format(hak))
        while True:
            if hak > 0 :
                tahmin = int(input("tahmin için 1-20 arasında bir sayı giriniz : "))
            else:
                print("sayıyı doğru tahmin edemediniz : Bulamadığınız sayı : {}".format(rastgeleSayi))
                break

            if tahmin != rastgeleSayi:
                hak -= 1
                if tahmin > rastgeleSayi:
                    print("lütfen daha küçük bir sayı giriniz. Kalan tahmin hakkınız : {}".format(hak))
                else:
                    print("lütfen daha büyük bir sayı giriniz. Kalan tahmin hakkınız : {}".format(hak))
            else:
                print("Tebrikler sayıyı buldunuz")
                break

        kontrol = input("Oyuna devam etmek 'E' veya çıkmak için 'H' giriniz : ")
        if kontrol == "E" or kontrol == "e":
            oyunDurumu = True
        else:
            oyunDurumu = False

sayiTahmin()
