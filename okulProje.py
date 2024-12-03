
okul={}


def sinif_ekle(okul:dict):
    sinif = input("Öğrencinin sınıfını giriniz :")
    sube = input("Öğrencinin şubesini giriniz :")
    ogrenci = input("Öğrencinin ismini giriniz :")


def sinif_listele(okul:dict):
    sinif = input("Öğrencinin sınıfını giriniz :")
    sube = input("Öğrencinin şubesini giriniz :")
    ogrenci = input("Öğrencinin ismini giriniz :")


def sube_ekle(okul:dict):
    pass


def sube_listele(okul:dict):
    pass


def ogrenci_ekle(okul:dict):
    sinif = input("Hangi sınıfa öğrenci ekleyeceksiniz :")
    sube = input("Hangi şubeye öğrenci ekleyeceksiniz :")
    while True:
        print("""
1- Yeni Öğrenci Ekle
2- Öğrenci Çıkar
3- Öğrenci İsmi Düzenle
4- Şubenin Öğrencilerini Listele
5- Ana Menüye Dön
""")
        sec = input("işleminizi seçiniz : ")
        if sec == "1":
            ogrenci = input("öğrenci ismini giriniz : ")
            okul[sinif][sube][ogrenci] = {}
            print("Yeni öğrenci ekleme işlemi başarılı")
        elif sec == "2":
            cikacakOgrenci = input("Çıkarılacak öğrenci ismini giriniz : ")
            okul[sinif][sube].pop(cikacakOgrenci)
            print("Öğrenci çıkarma işlemi başarılı")
        elif sec == "3":
            degisecekOgrenci = input("Düzenlemek istediğiniz öğrenci ismi : ")
            okul[sinif][sube].pop(degisecekOgrenci)
            isim = input("Öğrencinin yeni ismini giriniz : ")
            okul[sinif][sube][isim] = {}
            print("Öğrenci isim düzenleme işlemi başarılı")
        elif sec == "4":
            t = 0
            for i in okul[sinif][sube]:
                t+=1
                print("{}. {}".format(t,i))
        elif sec == "5":
            break


def ogrenci_listele(okul:dict):
    for i in okul:
        print("{}. sınıf : ".format(i))
        for t in okul[i]:
            print("{:>10} Şubesi".format(t))
            z=0
            for y in okul[i][t]:
                z+=1
                print("{:>20}. {}".format(z,y))


def ders_ekle(okul:dict):
    sinif = input("Öğrencinin sınıfını giriniz :")
    sube = input("Öğrencinin şubesini giriniz :")
    ogrenci = input("Öğrencinin ismini giriniz :")
    while True:
        print("""
    1- Yeni Ders Ekle
    2- Ders Çıkar
    3- Dersleri Listele
    4- Ana Menüye dön.""")
        sec = input("seçiminizi yapınız : ")



def ders_listele(okul:dict):
    pass


def not_ekle(okul:dict):
    pass


def not_goster(okul:dict):
    pass


def anaFonksiyon():
    menu="""
1- Sınıf Ekle
2- Sınıfları Listele
3- Şube Ekle
4- Şubeleri Listele
5- Ögrenci Ekle
6- Öğrenci Listele
7- Ders Ekle
8- Dersleri Listele
9- Not Ekle
10- Ders notlarını göster
11- Çıkış
"""
    print(menu)
    secim = input("Seçiminizi giriniz : ")
    if secim == "1":
        sinif_ekle(okul)
    elif secim == "2":
        sinif_listele(okul)
    elif secim == "3":
        sube_ekle(okul)
    elif secim == "4":
        sube_listele(okul)
    elif secim == "5":
        ogrenci_ekle(okul)
    elif secim == "6":
        ogrenci_listele(okul)
    elif secim == "7":
        ders_ekle(okul)
    elif secim == "8":
        ders_listele(okul)
    elif secim == "9":
        not_ekle(okul)
    elif secim == "10":
        not_goster(okul)
    elif secim == "11":
        quit()
    else:
        print("Hatalı giriş yaptınız")