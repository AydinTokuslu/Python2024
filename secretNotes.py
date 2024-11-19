
from cryptography.fernet import Fernet

'''''
message = "hello geeks"

key = Fernet.generate_key()

fernet = Fernet(key)

encMessage = fernet.encrypt(message.encode())

print("original string: ", message)
print("encrypted string: ", encMessage)

decMessage = fernet.decrypt(encMessage).decode()

print("decrypted string: ", decMessage)


'''
key = Fernet.generate_key()
fernet = Fernet(key)

def save_encrypt():
    title = input("please enter your title = ")
    secret = input("please enter your secret = ")
    master_key = input("please enter your master key = ")

    encoded = fernet.encrypt(secret.encode())
    return (encoded, master_key)


## And then to decode it:
def decrypt(encoded,master_key):
    master_key2 = input("please enter your master key = ")
    while True:
        if master_key2 == master_key:
            decoded = fernet.decrypt(encoded).decode()

        else:
            print("please enter the correct master key")
            continue
        return decoded

print(decrypt(save_encrypt()))

