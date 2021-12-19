from cryptography.fernet import Fernet

def generateKey():
    return Fernet.generate_key().decode()

def encrypt(data, key):
    f = Fernet(key)
    encrypted_data = f.encrypt(data.encode())
    return encrypted_data.decode()

def decrypt(data, key):
    f = Fernet(key)
    decrypted_data = f.decrypt(data.encode())
    return decrypted_data.decode()

key = generateKey()