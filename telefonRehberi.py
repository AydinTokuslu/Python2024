


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
    name = input("Lütfen aramak istediğiniz ismi giriniz: ")

    with open("telefon_rehberi.txt", mode="r", encoding="utf-8") as file:
        bilgiler = file.readlines()

        bulundu = False  # Kayıt bulunup bulunmadığını takip eder
        for bilgi in bilgiler:
            bilgi = bilgi.strip()  # Satır sonundaki boşlukları ve yeni satır karakterini temizler
            bilgi = bilgi.split(" ")  # Satırı boşluklara göre böl
            ad, soyad, tel_no = bilgi[0], bilgi[1], bilgi[2]

            if name == ad or name == soyad:
                print(ad + " " + soyad + " " + tel_no)
                bulundu = True  # Kayıt bulundu
                break  # Aranan kişi bulunursa döngüden çık

        if not bulundu:
            print("Aradığınız kişi kayıtlarda bulunmamaktadır. Ana menüye yönlendiriliyorsunuz!!!")


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
    silinecekIsim = input("Silinmesini istediğiniz kişinin ismini giriniz : ")

    with open("telefon_rehberi.txt", mode="r", encoding="utf-8") as file:
        bilgiler = file.readlines()

        bulundu = False  # Kayıt bulunup bulunmadığını takip eder
        for bilgi in bilgiler:
            bilgi = bilgi.strip()  # Satır sonundaki boşlukları ve yeni satır karakterini temizler
            bilgi = bilgi.split(" ")  # Satırı boşluklara göre böl
            ad, soyad, tel_no = bilgi[0], bilgi[1], bilgi[2]

            if silinecekIsim == ad or silinecekIsim == soyad:
                print("Silinecek kişi : {}  {}  {}".format(ad,soyad,tel_no))
                bulundu = True  # Kayıt bulundu
                """
                with open("telefon_rehberi.txt", "r") as f:
                    lines = f.readlines()
                with open("telefon_rehberi.txt", "w") as f:
                    for line in lines:
                        line = line.strip()  # Satır sonundaki boşlukları ve yeni satır karakterini temizler
                        line = line.split(" ")  # Satırı boşluklara göre böl
                        ad, soyad, tel_no = line[0], line[1], line[2]
                        if ad != silinecekIsim or soyad != silinecekIsim:
                        #if line.strip("\n") != silinecekIsim:
                            f.write(ad+"\t")
                            f.write(soyad+"\t")
                            f.write(tel_no+"\n")
                """
                print("")
                print(f"{silinecekIsim} kayıtlardan silinmiştir.")
                #kayitlariListele()
                break  # Aranan kişi bulunursa döngüden çık

        if not bulundu:
            print("Aradığınız kişi kayıtlarda bulunmamaktadır. Ana menüye yönlendiriliyorsunuz!!!")


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