import web3

class BlockchainInterface:
    def __init__(self, blockchain_url):
        self.blockchain_url = blockchain_url
        self.web3 = web3.Web3(web3.providers.HttpProvider(self.blockchain_url))

    def store_data(self, data):
        # Store data on blockchain using Web3
        self.web3.eth.sendTransaction({'from': '0x...', 'to': '0x...', 'data': data})

    def check_data(self, data_hash):
        # Check if data exists on blockchain using Web3
        return self.web3.eth.getStorageAt('0x...', data_hash) != '0x0'
