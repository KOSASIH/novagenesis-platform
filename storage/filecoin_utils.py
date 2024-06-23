import filecoin

class FilecoinUtils:
    def __init__(self, filecoin_url):
        self.filecoin_url = filecoin_url
        self.client = filecoin.Client(self.filecoin_url)

    def store_data(self, data):
        # Store data on Filecoin usingfilecoin library
        cid = self.client.put(data)
        return cid

    def retrieve_data(self, cid):
        # Retrieve data from Filecoin using filecoin library
        data = self.client.get(cid)
        return data
