import hashlib

class IdentityManager:
    def __init__(self, blockchain_interface):
        self.blockchain_interface = blockchain_interface

    def create_identity(self, user_data):
        # Hash user data and store on blockchain
        user_hash = hashlib.sha256(user_data.encode()).hexdigest()
        self.blockchain_interface.store_data(user_hash)
        return user_hash

    def verify_identity(self, user_hash):
        # Check if user hash exists on blockchain
        return self.blockchain_interface.check_data(user_hash)
