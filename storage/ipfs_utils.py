import ipfshttpclient

class IpfsUtils:
    def __init__(self, ipfs_url):
        self.ipfs_url = ipfs_url
        self.client = ipfshttpclient.connect(self.ipfs_url)

    def store_file(self, file_path):
        # Store file on IPFS using ipfshttpclient
        file_hash = self.client.add(file_path)
        return file_hash

    def retrieve_file(self, file_hash):
        # Retrieve file from IPFS using ipfshttpclient
        file_path = self.client.get(file_hash)
        return file_path
