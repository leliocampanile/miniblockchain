import hashlib as hasher
import datetime as date

class Block:
    def __init__(self, index, timestamp, data, previous_hash):
        self.index = index
        self.timestamp = timestamp
        self.data = data
        self.previous_hash = previous_hash
        self.hash = self.hash_block()


    def hash_block(self):
        sha = hasher.sha256()
        sha.update(str(self.index).encode('utf-8') + 
                   str(self.timestamp).encode('utf-8') +
                   str(self.data).encode('utf-8') + 
                   str(self.previous_hash).encode('utf-8'))
        return sha.hexdigest()
    
def create_genesis_block():
    # first block generation
    return Block(0, date.datetime.now(), "Genesis Block", "0")

def next_block(last_block):
    next_index = last_block.index + 1
    next_timestamp = date.datetime.now()
    next_data = "data of the block n. " + str(next_index)
    next_hash = last_block.hash
    return Block(next_index, next_timestamp, next_data, next_hash)

if __name__ == "__main__":
    # create blockchain and add first block
    blockchain = [create_genesis_block()]
    previous_block = blockchain[0]

    n_blocks_to_add = 20

    for i in range(0, n_blocks_to_add):
        block_to_add = next_block(previous_block)
        blockchain.append(block_to_add)
        previous_block = block_to_add
        print("Block %d added to the blockchain" % block_to_add.index)
        print("Hash: %s \n" % block_to_add.hash)
    



