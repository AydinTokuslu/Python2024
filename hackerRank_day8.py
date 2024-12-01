# Given n names and phone numbers, assemble a phone book that maps friends' names to their respective phone numbers.
# You will then be given an unknown number of names to query your phone book for.
# For each name queried, print the associated entry from your phone book on a new line in the form name=phoneNumber;
# if an entry for name is not found, print Not found instead.
#
# Note: Your phone book should be a Dictionary/Map/HashMap data structure.

#input
# 3
# sam 99912222
# tom 11122222
# harry 12299933
# sam
# edward
# harry

#output
# sam=99912222
# Not found
# harry=12299933

if __name__ == '__main__':
    n = int(input())
    phone_book = {("sam", 99912222), ("tom", 11122222), ("harry", 12299933)}
    print(phone_book)
    for i in range(1,n+1):
        print(phone_book[i])
        if phone_book[i] == i:
            print(f"{i} = {phone_book[i]} ")
        else:
            print("Not found")



