import hashlib as hasher
import datetime as date

class BlockchainIterator:
    # This class is for iterate the blockchain's blocks
    def __init__(self, blockchain):
        self._blockchain = blockchain
        self._index = 0

    def __next__(self):
        # return the next block in the blockchain
        if self._index < len(self._blockchain._chain) :
            result = self._blockchain._chain[self._index]
            self._index +=1
            return result
        raise StopIteration

class Block:
    def __init__(self, index, timestamp, data, previous_hash):
        self.index = index
        self.timestamp = timestamp
        self.data = data
        self.previous_hash = previous_hash
        self.hash = self.hash_block()

    def __str__(self):
        return "Block n. %d with hash %s and previous has %s" % (self.index, 
                self.hash, self.previous_hash)

    def hash_block(self):
        sha = hasher.sha256()
        sha.update(str(self.index).encode('utf-8') + 
                   str(self.timestamp).encode('utf-8') +
                   str(self.data).encode('utf-8') + 
                   str(self.previous_hash).encode('utf-8'))
        return sha.hexdigest()
    
    def get_block_data(self):
        return {'index': self.index,
                'timestamp': self.timestamp,
                'data': self.data,
                'previous_hash': self.previous_hash,
                'hash': self.hash}
    
class Blockchain:
    def __init__(self):
        # add first block to the chain
        self._chain = [self._create_genesis_block()]
        #self._next_block = self._create_next_block()
        #self.validate_chain()
        #self.data = []
    
    def __iter__(self):
        # iterate the blockchain
        return BlockchainIterator(self)

    
    def _create_genesis_block(self):
        # first block generation
        return Block(0, date.datetime.now(), "Genesis Block", "0")
    
    def _create_next_block(self):
        last_block = self._chain[-1]
        next_index = last_block.index + 1
        next_timestamp = date.datetime.now()
        next_data = "data of the block n. " + str(next_index)
        next_hash = last_block.hash
        return Block(next_index, next_timestamp, next_data, next_hash)
    
    def add_new_block(self):
        block_to_add  = self._create_next_block()
        self._chain.append(block_to_add)
        return 1
    





def next_block(last_block):
    next_index = last_block.index + 1
    next_timestamp = date.datetime.now()
    next_data = "data of the block n. " + str(next_index)
    next_hash = last_block.hash
    return Block(next_index, next_timestamp, next_data, next_hash)

if __name__ == "__main__":
    ''' create blockchain and add first block
    blockchain = [create_genesis_block()]
    previous_block = blockchain[0]

    n_blocks_to_add = 20

    for i in range(0, n_blocks_to_add):
        block_to_add = next_block(previous_block)
        blockchain.append(block_to_add)
        previous_block = block_to_add
        print("Block %d added to the blockchain" % block_to_add.index)
        print("Hash: %s \n" % block_to_add.hash)
    '''
    b = Blockchain()
    for i in range(10):
        b.add_new_block()
    for block in b:
        print(block)