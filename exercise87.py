# yazı-tura atarak yazı mı tura mı olduğunu bilmek

import random

yazi=0
tura=0

para_yuzeyi=["tura","yazi"]
atilcak_para_sayisi=int(input("kaç kere atmak istiyorsunuz : "))

while atilcak_para_sayisi>0:
    para_ustu=random.choice(para_yuzeyi)
    #print(para_ustu)
    if para_ustu=="tura" or para_ustu=="Tura":
        tura+=1
        print("tura geldi!!")
    else:
        yazi+=1
        print("yazi geldi!!!")
    atilcak_para_sayisi-=1

print("Tura sayısı : {}\nYazi sayısı : {}".format(tura,yazi))