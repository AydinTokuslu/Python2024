from cryptography.fernet import Fernet


key = Fernet.generate_key()
fernet = Fernet(key)

def save_encrypt():

    title = input("please enter your title = ")
    secret = input("please enter your secret = ")
    master_key = input("please enter your master key = ")
    encoded = fernet.encrypt(secret.encode())
    print(encoded)
    decrypt(encoded, master_key)


## And then to decode it:
def decrypt(encoded,master_key):
    while True:
        try:
            master_key2 = input("please enter your master key = ")
            if master_key2 == master_key:
                decoded = fernet.decrypt(encoded).decode()
                print(decoded)
                break
            else:
                fake_decrypt(master_key2)
                print("please enter the correct master key!!!!!")
        except:
            continue


def fake_decrypt(str2):
    encoded = fernet.encrypt(str2.encode())
    print(encoded)

save_encrypt()