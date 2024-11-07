#def toplama(a,b):
#    print(a,b)

#x = toplama(3,4)
#print(x)

#def usselIslem(x=5,y=3):
#    print(x ** y)

#usselIslem()

#def myLoop(*args):
#    for element in args:
#        print(element / 2)

#myLoop(3,2,1,5,3,4)

def myFunc(num):
    return num ** 3

myList = [2,3,4,5,6]
newList = []
for i in myList:
    newList.append(myFunc(i))
print(newList)