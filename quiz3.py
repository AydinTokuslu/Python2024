#1) Aşağıdaki kodun çıktısı ne olacaktır?
#def toplama(a,b):
#    print(a,b)

#x = toplama(3,4)
#print(x)

#2) Aşağıdaki kodun çıktısı ne olacaktır?
#def usselIslem(x=5,y=3):
#    print(x ** y)

#3) Aynı fonksiyonu aşağıdaki gibi çağırırsak çıktı ne olur?
#usselIslem()

#4) Aşağıdaki kodun çıktısı ne olacaktır?
#def myLoop(*args):
#    for element in args:
#        print(element / 2)

#myLoop(3,2,1,5,3,4)

#5) Aşağıdaki dizide belirtilen rakamları, myFunction fonksiyonuna tabi tutup, yeni bir dizi oluşturunuz
#def myFunc(num):
#    return num ** 3

#myList = [2,3,4,5,6]
#newList = []
#for i in myList:
#    newList.append(myFunc(i))
#print(newList)

#print(list(map(myFunc,myList)))

#6) Aşağıdaki string dizisinde, içinde sadece XYZ geçen barkodları gösterecek yeni bir liste oluşturunuz
#barkodDizisi = ["ABC231","SA3123XYZ","XYZA123Q","QRE1231KJ","X112QGL"]
#print(list(filter(lambda string : "XYZ" in string, barkodDizisi)))

#7) Aşağıdaki kodu okursanız, ornekFonksiyon çalıştırıldığında en altta yazdırılan print size neyi yazdıracaktır?
myVar = "Atil Samancioglu"


def ornekFonksiyon():
    myVar = "Atil"

    def digerFonksiyon():
        print(myVar)

    digerFonksiyon()

ornekFonksiyon()