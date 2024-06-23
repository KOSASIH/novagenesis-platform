import cryptography

class DataEncryptor:
    def __init__(self, encryption_key):
        self.encryption_key = encryption_key

    def encrypt_data(self, data):
        # Encrypt data using cryptography library
        encrypted_data = cryptography.encrypt(data, self.encryption_key)
        return encrypted_data

    def decrypt_data(self, encrypted_data):
        # Decrypt data using cryptography library
        decrypted_data = cryptography.decrypt(encrypted_data, self.encryption_key)
        return decrypted_data
