
hesap_bakiyesi = 2000

def bankaIslemleri():
    while True:
        menu = """
        1- Para Çekme
        2- Para Yatırma
        3- Bakiye Görüntüleme
        """


        secim = int(input("işlem yapmak için 1'i çıkmak için 0'ı tuşlayınız : "))
        if secim == 1:
            cekilecekMiktar = int(input("lütfen çekmek istediğiniz bakiyeyi giriniz : "))
            if cekilecekMiktar > hesap_bakiyesi:
                print("hesabınızda yeterli limitiniz yoktur.")
                secim = int(input("Para yatırmak için 1'i çıkmak için 0'ı giriniz : "))
                if secim:
                    paraYatirma()
                else:
                    exit()
            else:
                paraCekme(cekilecekMiktar)
        elif secim == 0:
            print("Çıkış yaptınız. tekrar bekleriz, iyi günler")
            break
        else:
            print("yanlış sayı  girdiniz, tekrar deneyiniz.")


def paraYatirma():
    global hesap_bakiyesi
    yatirilacakPara = int(input("lütfen yatırmak istediğiniz miktarı giriniz : "))
    hesap_bakiyesi += yatirilacakPara
    print("yeni bakiyeniz : {}".format(hesap_bakiyesi))

def paraCekme(cekilecekMiktar):
    global hesap_bakiyesi
    hesap_bakiyesi -= cekilecekMiktar
    print("yeni bakiyeniz : {}".format(hesap_bakiyesi))

def


bankaIslemleri()