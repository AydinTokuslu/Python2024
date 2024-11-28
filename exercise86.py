def faktoriyelAl(sayi):
    faktoriyel=1
    metin = ""
    for i in range(1,sayi+1):
        faktoriyel=faktoriyel * i
        if sayi > i+1:
            metin += str(sayi - i)+" - "
    return f"{sayi} sayısının faktöriyeli = {sayi} - {metin}1 = {faktoriyel}"

print(faktoriyelAl(6))