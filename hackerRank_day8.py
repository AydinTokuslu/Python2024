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

# Function to create a phone book and handle queries
def phone_book():
    n = int(input())  # Number of entries in the phone book
    phone_book = {}  # Dictionary to store the phone book

    # Reading phone book entries
    for _ in range(n):
        entry = input().split()
        name, phone = entry[0], entry[1]
        phone_book[name] = phone

    # Processing queries
    while True:
        try:
            query = input().strip()
            if query in phone_book:
                print(f"{query}={phone_book[query]}")
            else:
                print("Not found")
        except EOFError:
            break  # Exit the loop when no more input is provided

# Run the phone book function
if __name__ == "__main__":
    phone_book()



