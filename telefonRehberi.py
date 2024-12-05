


def display_menu():
    print("""
1-Kayıtları Listele
2-Kayıt Ara
3-Kayıt Ekle
4-Kayıt Sil
5-Çıkış
""")


def kayitlariListele():
    with open("telefon_rehberi.txt", mode="r", encoding="utf-8") as file:
        bilgiler = file.readlines()
        for bilgi in bilgiler:
            bilgi = bilgi.replace("\n","")
            bilgi = bilgi.split(" ")
            ad = bilgi[0]
            soyad = bilgi[1]
            tel_no = bilgi[2]
            print(ad+" "+soyad+" "+ tel_no)



def kayitAra():
    print("")
    name = input("lütfen aramak istediğiniz ismi giriniz : ")

    with open("telefon_rehberi.txt", mode="r", encoding="utf-8") as file:
        bilgiler = file.readlines()
        #print(bilgiler)
        for bilgi in bilgiler:
            bilgi = bilgi.replace("\n","")
            bilgi = bilgi.split(" ")
            ad = bilgi[0]
            soyad = bilgi[1]
            tel_no = bilgi[2]

            if name == ad or name == soyad:
                print(ad+" "+soyad+" "+ tel_no)
            else:
                print("Aradığınız kişi kayıtlarda bulunmamaktadır. Ana menüye yönlendiriliyorsunuz!!!")
    main()



name = ""
surname = ""
telNo = ""

records_list = []
def kayitEkle():
    print("yeni kayıt ekle")
    global name
    global surname
    global telNo
    name = input("İsim : ")
    surname = input("Soyisim : ")
    telNo = input("Telefon numarası : ")
    print(f"Yeni kayıt : {name} {surname} {telNo}\nYeni Kayıt Eklendi")
    with open("telefon_rehberi.txt", mode="a", encoding="utf-8") as file:
       file.write(name+" "+surname+" "+telNo+"\n")
       records_list.append(file)
    print(records_list)

def kayitSil():
    pass


def main():
    while True:
        display_menu()
        secim = input("lütfen menüden seçiminizi yapınız : ")
        if secim == "1":
            kayitlariListele()
        elif secim == "2":
            kayitAra()
        elif secim == "3":
            kayitEkle()
        elif secim == "4":
            kayitSil()
        else:
            break

main()