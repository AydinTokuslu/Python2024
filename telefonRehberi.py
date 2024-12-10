


def display_menu():
    print("""
1-Kayıtları Listele
2-Kayıt Ara
3-Kayıt Ekle
4-Kayıt Sil
5-Çıkış
""")


def kayitlariListele():
    try:
        with open(FILENAME, mode="r") as file:
            bilgiler = file.readlines()
            if not bilgiler:
                print("Kayıtlı kişi bulunmamaktadır.")
            else:
                for i, bilgi in enumerate(bilgiler, start=1):
                    bilgi = bilgi.strip()
                    if not bilgi:
                        continue
                    parcalar = bilgi.split(" ")
                    if len(parcalar) != 3:
                        print(f"Geçersiz kayıt (Satır {i}): {bilgi}")
                        continue
                    ad, soyad, tel_no = parcalar
                    print(f"{ad} {soyad} {tel_no}")
    except FileNotFoundError:
        print("Telefon rehberi dosyası bulunamadı.")

"""
def kayitlariListele():
    try:
        with open(FILENAME, mode="r") as file:
            bilgiler = file.readlines()
            if not bilgiler:
                print("Kayıtlı kişi bulunmamaktadır.")
            else:
                for bilgi in bilgiler:
                    bilgi = bilgi.strip()
                    ad, soyad, tel_no = bilgi.split(" ")
                    print(f"{ad} {soyad} {tel_no}")
    except FileNotFoundError:
        print("Telefon rehberi dosyası bulunamadı.")
"""

def kayitAra():
    print("")
    name = input("Lütfen aramak istediğiniz ismi giriniz: ")

    with open(FILENAME, mode="r") as file:
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


#name = ""
#surname = ""
#telNo = ""

FILENAME = "telefon_rehberi.txt"


def kayitEkle():
    print("Yeni kayıt ekle")

    while True:
        name = input("İsim: ").strip()
        if not name:
            print("İsim boş olamaz. Lütfen tekrar girin.")
            continue

        surname = input("Soyisim: ").strip()
        if not surname:
            print("Soyisim boş olamaz. Lütfen tekrar girin.")
            continue

        telNo = input("Telefon numarası: ").strip()
        if not telNo.isdigit():
            print("Telefon numarası sadece rakamlardan oluşmalıdır. Lütfen tekrar girin.")
            continue

        break

    # Kayıt ekleme işlemi
    with open(FILENAME, mode="a") as file:
        file.write(f"{name} {surname} {telNo}\n")

    print(f"Yeni kayıt eklendi: {name} {surname} {telNo}")


def kayitSil():
    silinecekIsim = input("Silinmesini istediğiniz kişinin ismini veya soyismini giriniz: ").strip()

    try:
        with open(FILENAME, mode="r") as file:
            bilgiler = file.readlines()

        bulunan_kisiler = []
        yeni_bilgiler = []

        # Tüm kayıtları kontrol et
        for bilgi in bilgiler:
            bilgi = bilgi.strip()
            if not bilgi:
                continue  # Boş satırları atla

            parcalar = bilgi.split(" ")
            if len(parcalar) != 3:
                yeni_bilgiler.append(bilgi + "\n")  # Hatalı formatlı kayıtları geri ekle
                continue

            ad, soyad, tel_no = parcalar
            if silinecekIsim == ad or silinecekIsim == soyad:
                bulunan_kisiler.append((ad, soyad, tel_no))
            else:
                yeni_bilgiler.append(f"{ad} {soyad} {tel_no}\n")  # Diğer kayıtları ekle

        if not bulunan_kisiler:
            print("Aradığınız kişi kayıtlarda bulunmamaktadır.")
            return

        # Aynı isim veya soyadı taşıyan kişileri listele
        print("Eşleşen kişiler:")
        for i, (ad, soyad, tel_no) in enumerate(bulunan_kisiler, start=1):
            print(f"{i}: {ad} {soyad} {tel_no}")

        # Kullanıcıdan seçim yapmasını iste
        try:
            secim = int(input("Silmek istediğiniz kaydın numarasını seçiniz (iptal için 0): "))
            if secim == 0:
                print("İşlem iptal edildi.")
                return

            secilen_kisi = bulunan_kisiler[secim - 1]  # Kullanıcının seçtiği kaydı al
            print(f"Silinecek kişi: {secilen_kisi[0]} {secilen_kisi[1]} {secilen_kisi[2]}")
        except (ValueError, IndexError):
            print("Geçersiz seçim. İşlem iptal edildi.")
            return

        # Seçilen kaydı dosyadan sil
        yeni_bilgiler = [
            f"{ad} {soyad} {tel_no}\n"
            for ad, soyad, tel_no in
            [(bilgi.split(" ")[0], bilgi.split(" ")[1], bilgi.split(" ")[2]) for bilgi in bilgiler]
            if (ad, soyad, tel_no) != secilen_kisi
        ]

        with open(FILENAME, mode="w") as file:
            file.writelines(yeni_bilgiler)

        print(f"{secilen_kisi[0]} {secilen_kisi[1]} kayıtlardan silinmiştir.")

    except FileNotFoundError:
        print("Telefon rehberi dosyası bulunamadı.")


def main():
    while True:
        display_menu()
        secim = input("Lütfen menüden seçiminizi yapınız: ")
        if secim == "1":
            kayitlariListele()
        elif secim == "2":
            kayitAra()
        elif secim == "3":
            kayitEkle()
        elif secim == "4":
            kayitSil()
        elif secim == "5":
            print("Çıkış yapılıyor. Hoşça kalın!")
            break
        else:
            print("Geçersiz seçim, lütfen tekrar deneyin.")

main()