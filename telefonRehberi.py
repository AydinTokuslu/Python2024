


def display_menu():
    print("""
1-Kayıtları Listele
2-Kayıt Ara
3-Kayıt Ekle
4-Kayıt Sil
5-Çıkış
""")


def kayitlariListele():
    pass


def kayitAra():
    pass


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