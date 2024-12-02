import time


hastaAdi = ""
hastaSoyadi = ""
hastaSikayeti = ""


doktor_listesi = {"Hakan" : "Allerji",
                  "Mithat" : "Allerji",
                  "Cemil" : "Basagrisi",
                  "Elif" : "Diyabet",
                  "Hande" : "Diyabet",
                  "Nuray" : "Sogukalginligi",
                  "Fatma" : "Sogukalginligi",
                  "Aydın" : "Migren",
                  "Enis" : "Migren",
                  "Hüseyin" : "Kalp Hastaliklari",
                  "Hüsamettin" : "Kalp Hastaliklari",
                  "Fırat" : "Kalp Hastaliklari",
                  "Hilal" : "Cocuk Hastaliklari",
                  "Bilal" : "Cocuk Hastaliklari",
                  "Aslı" : "Genel Cerrahi",
                  "Asuman" : "Genel Cerrahi",
                  "Sare" : "Genel Cerrahi" }

def hasta_giris():
    global hastaAdi
    global hastaSoyadi
    global hastaSikayeti
    dosya = open("hasta_bilgileri.txt", "a", encoding="utf-8")
    hastaAdi = input("Lütfen hasta adını giriniz : ")
    hastaSoyadi = input("Lütfen hasta soyadını giriniz : ")
    hastaSikayeti = input("Lütfen yukarıdaki listeden hasta şikayetini giriniz : ")
    print("Kaydınız tamamlanmıştır. Ana menüye yönlendiriliyorsunuz...")
    dosya.write(hastaAdi+"/"+hastaSoyadi+"/"+hastaSikayeti+"\n")
    main()
    dosya.close()
    return hastaAdi, hastaSoyadi, hastaSikayeti


def hasta_bilgileri_goruntuleme():
    with open("hasta_bilgileri.txt", "r", encoding="utf-8") as file:
        bilgiler = file.readlines()
        for bilgi in bilgiler:
            bilgi = bilgi.replace("\n", "")
            bilgi = bilgi.split("/")
            ad = bilgi[0]
            soyad = bilgi[1]
            bolum = bilgi[2]
            dosya_m = open("Migren_hastaliklari.txt", "a", encoding="utf-8")
            if bolum == "Migren":
                dosya_m.write(ad)
                dosya_m.write(" " * (25 - len(ad)))
                dosya_m.write(soyad)
                dosya_m.write(" " * (25 - len(soyad)))
                dosya_m.write(bolum)
                dosya_m.write(" " * (25 - len(bolum)))
                dosya_m.write("\n")
    file.close()


def recete_kontrolu():
    pass


def randevu_al():
    print("Görevli Doktor Listesi : ")
    print("S.No : Doktor İsmi :         Branşı : ")
    print("-------------------------------------")
    a = 0
    for i in doktor_listesi.items():
        a += 1
        print("{:<3}-   Dr.{:<10} ------> {:<10}".format(a, i[0], i[1]))


def odemek():
    pass


def main():
    while True:
        print("""
    1-Hasta Bilgilerini Görüntüleme
    2-Reçete Sorgulama
    3-Randevu Almak
    4-Ödeme
    5-Çıkış  
        """)
        secim = input("Lütfen seçiminizi yapınız : ")
        if secim == "1":
            hasta_bilgileri_goruntuleme()
        elif secim == "2":
            recete_kontrolu()
        elif secim == "3":
            randevu_al()
        elif secim == "4":
            odemek()
        elif secim == "5":
            quit()
        else:
            print("Yanlış tercihte bulundunuz. Tekrar deneyiniz.")



randevu_al()

#hasta_giris()