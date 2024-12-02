import time

#kullanıcından hasta ismi alınsın.
#1- ilaç listesi oluşturun (Aspirin, Cibadrex, vb)
#2- hastalık listesi oluşturalım (alerji, Başağrısı,vb.)
#3- hastalığa ve ilaca bağlı bir reçete oluşturalım
#4- reçeteleri ana listin içine atalım


hastaAdi = ""
hastaSoyadi = ""
hastaSikayeti = ""
ilac_ode = 0
hasta_list = []


recete_list = {1 : "Parol",
               2 : "Aspirin",
               3 : "Glifor",
               4 : "Aferin",
               5 : "Majezik",
               6 : "Ecoprin",
               7 : "Beloc",
               8 : "Calpol",
               9 : "Ventolin",
               }

hastalikList=["Alerji","Basagrisi","Diyabet","Sogukalginligi","Migren","Kalp Hastaliklari","Cocuk Hastaliklari","Genel Cerrahi"]
ilac_fiyatlari = {"Parol" : 50,
                  "Aspirin" : 40,
                  "Glifor" : 65,
                  "Aferin" : 55,
                  "Majezik" : 80,
                  "Ecoprin" : 90,
                  "Beloc" : 120,
                  "Calpol" : 100,
                  "Ventolin" : 150
                  }

doktor_listesi = {"Hakan" : "Alerji",
                  "Mithat" : "Alerji",
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


def hastalıkListesi():
    print("Hastalık çeşitleri : ")
    print("--------------------")
    for i in hastalikList:
        print(i)


def hasta_giris():
    global hastaAdi
    global hastaSoyadi
    global hastaSikayeti
    dosya = open("hasta_bilgileri.txt", "a", encoding="utf-8")
    hastalıkListesi()
    print("")
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
            #print("Hasta Bilgileri")
            #print("-----------------")
            print(ad+"  "+ soyad+"  "+bolum)
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


def recete_kontrolu(ilac_ode):
    recete_k = True
    while recete_k:
        recete_no = int(input("Lütfen reçete numaranızı giriniz (1-8) : "))
        if recete_no in recete_list:
            print("İstediğiniz ilaç mevcuttur. Reçete ekranına yönlendiriliyorsunuz...")
            print(f"Reçeteniz : {recete_list[recete_no]}")
            recete_k = False
            sec = input("İlacınızı satın almak için 1'i, ana menüye dönmek için 2'yi tuşlayınız. ")
            if sec == "1":
                if recete_list[recete_no] in ilac_fiyatlari.keys():
                    print(f"İlacınız olan {recete_list[recete_no]}'in fiyatı : {ilac_fiyatlari[recete_list[recete_no]]}'tldir.")
                ilac_ode += ilac_fiyatlari[recete_list[recete_no]]
                print(f"Yapacağınız toplma ödeme : {ilac_ode} tldir.")
                sec = input("Ödeme yapmak için 1'i, başka bir ilaç almak için 2'yi tuşlayınız : ")
                if sec == "1":
                    odemek(ilac_ode)
                elif sec == "2":
                    recete_kontrolu(ilac_ode)
                else:
                    print("Yanlış tercihte bulundunuz. tekrar deneyiniz.")
            elif sec == "2":
                main()
            else:
                print("Yanlış tercihte bulundunuz, tekrar giriş yapıp deneyiniz.")
        else:
            secim = input("İstediğiniz ilaç maalesef mevcut değildir. Tekrar giriş yapmak için 1'i, çıkış için 2'yi tuşlayınız.")
            if secim == "1":
                hasta_giris()
            elif secim == "2":
                quit()
            else:
                print("Yanlış seçim yaptınız. çıkışa yönlendiriiyorsunuz. ")
                quit()


def randevu_al():
    print("Görevli Doktor Listesi : ")
    print("S.No : Doktor İsmi :         Branşı : ")
    print("-------------------------------------")
    a = 0
    for i in doktor_listesi.items():
        a += 1
        print("{:<3}-   Dr.{:<10} ------> {:<10}\n".format(a, i[0], i[1]))
    doktor = input("Lütfen muayene olmak istediğiniz doktor ismini DR ünvanı olmadan giriniz : ")
    if doktor in doktor_listesi.keys():
        muayene_gun = input("Lütfen muayene olmak istediğiniz günü giriniz : ")
        muayene_saati = input("Lütfen muayene olmak istediğiniz saati giriniz : \n")
        print(f"Sayın {hastaAdi} {hastaSoyadi}, {hastaSikayeti} şikayeti sebebi ile yapmış olduğunuz muayeneniz Dr.{doktor} ile {muayene_gun} günü ve saat {muayene_saati}'de yapılacaktır.")
    else:
        print("yanlış doktor ismi girdiniz, tekrar deneyiniz.")


def odemek(ilac_ode):
    print(f"Ödemeniz gereken toplam tutar : {ilac_ode}")
    sec = input("Ödemenizi kredi kartı ile ödemek için 1'i, havale ile ödemek için 2'yi tuşlayınız")
    if sec == "1":
        kartNo = input("Lütfen TR yazmadan ve boşluk bırakmadan 16 haneli kart numaranızı giriniz : ")
        if len(kartNo) != 16:
            print("Eksik veya fazla raka girişi yaptınız")
            print("Lütfen TR yazmadan ve boşluk bırakmadan 16 haneli kart numaranızı giriniz :")
            odemek(ilac_ode)
        elif len(kartNo) == 16 :
            print("Kart üzerinde yazan Ad ve Soyad bilgilerini giriniz : ")
            print("Kart üzerinde yazan son kullanma tarihini giriniz : ")
            print("Kart üzerinde yazan güvenlik numarasını giriniz : ")
            print(f"Ödemeniz gereken toplam tutar : {ilac_ode}")
            print("Ödemeniz başarı ile yapılmıştır. Teşekkür eder, yine bekleriz. Ana menüye yönlendiriliyorsunuz...")
            main()
    elif sec == "2":
        print("Havala yapacağınız banka bilgileri aşağıda belirtilmiştir. Ödeme sonrası bilgi vermeyi unutmayınız")
        print("TR1234 5678 9000 0123")
        print("Havale işlemi için teşekkür eder, yine bekleriz. Ana menüye yönlendiriliyorsunuz...")
        main()
    else:
        print("Yanlış işlem girdiniz. İşleminizi tekrar ediniz. ")
        odemek(ilac_ode)

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
            recete_kontrolu(ilac_ode)
        elif secim == "3":
            randevu_al()
        elif secim == "4":
            odemek(ilac_ode)
        elif secim == "5":
            quit()
        else:
            print("Yanlış tercihte bulundunuz. Tekrar deneyiniz.")



#randevu_al()

hasta_giris()