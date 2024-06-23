class AccessController:
    def __init__(self, identity_manager):
        self.identity_manager = identity_manager

    def grant_access(self, user_hash, resource):
        # Check if user has access to resource
        if self.identity_manager.verify_identity(user_hash):
            # Grant access using smart contract
            self.blockchain_interface.grant_access(user_hash, resource)
            return True
        return False

    def revoke_access(self, user_hash, resource):
        # Revoke access using smart contract
        self.blockchain_interface.revoke_access(user_hash, resource)
