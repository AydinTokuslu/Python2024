#x = 5
#y = 3
#z = 6

#print(x > y and z > x)
#print(x < y or z > y)

#4) Aşağıdaki sözlükte, değerler içinde c harfinin geçip geçmediğini gösteren bir if koşulu yazınız
#my_dictionary = {"k1":10,"k2k":"a","k32":30,"k4":"c"}

#if "c" in my_dictionary.values():
#    print("yes")

#5) Aşağıdaki sözlükte, anahtarlar içinde a harfinin geçip geçmediğini gösteren bir if koşulu yazınız
#my_other_dictionary = {"b":203,"c":"a","a":400,"d":"f"}
#if "a" in my_other_dictionary.keys():
#    print("a harfi key bölümünde geçiyor")
#elif "a" in my_other_dictionary.values():
#    print("a harfi value bölümünde geçiyor.")
#else:
#    print("a harfi geçmiyor.")

#6) Aşağıdaki listedeki sayılardan sadece çift sayı olanları yazdıran bir kod yazınız.
#my_numbers = [1,2,3,4,5,6,19,20,32,21,20,1111,23,24]
#cift_sayilar = []
#for i in my_numbers:
#    if i % 2 == 0 :
#        if i not in cift_sayilar:
#            cift_sayilar.append(i)
#        else:
#            continue
#print(cift_sayilar)

#r_list = [3,2,5,8,4,6,9,12]
#cevre = []
#pi = 3.14
#for i in r_list:
#    yeni_cevre = 2 * pi * i
#    cevre.append(yeni_cevre)
#print(cevre)

#age_name_list = [("Ahmet",30),("Ayse",24),("Mehmet",40),("Fatma",29)]
#yas_list = []

#for isim,yas in age_name_list:
#    yas_list.append(yas)
#print(yas_list)

#from random import randint
#metal_list = ["Metallica","Iron Maiden","Dream Theater","Megadeth","AC/DC"]
#print(metal_list[randint(0,len(metal_list)-1)])

number_list = [5,7,18,21,20,10,405,24]
print([num % 2 == 0 for num in number_list])








