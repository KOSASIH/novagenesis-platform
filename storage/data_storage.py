class DataStorage:
    def __init__(self, ipfs_utils, filecoin_utils):
        self.ipfs_utils = ipfs_utils
        self.filecoin_utils = filecoin_utils

    def store_data(self, data):
        # Store data on IPFS and Filecoin
        ipfs_hash = self.ipfs_utils.store_file(data)
        filecoin_cid = self.filecoin_utils.store_data(data)
        return ipfs_hash, filecoin_cid

    def retrieve_data(self, ipfs_hash, filecoin_cid):
        # Retrieve data from IPFS and Filecoin
        data = self.ipfs_utils.retrieve_file(ipfs_hash)
        if not data:
            data = self.filecoin_utils.retrieve_data(filecoin_cid)
        return data
