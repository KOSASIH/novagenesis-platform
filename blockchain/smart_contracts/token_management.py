class TokenManager:
    def __init__(self, blockchain_interface):
        self.blockchain_interface = blockchain_interface

    def create_token(self, user_hash):
        # Create token using smart contract
        token = self.blockchain_interface.create_token(user_hash)
        return token

    def verify_token(self, token):
        # Verify token using smart contract
        return self.blockchain_interface.verify_token(token)
