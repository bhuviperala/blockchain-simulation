import hashlib
import time

class Block:
    def __init__(self, index, timestamp, data, previous_hash=''):
        self.index = index
        self.timestamp = timestamp
        self.data = data
        self.previous_hash = previous_hash
        self.nonce = 0
        self.hash = self.calculate_hash()

    def calculate_hash(self):
        block_string = f"{self.index}{self.timestamp}{self.data}{self.previous_hash}{self.nonce}"
        return hashlib.sha256(block_string.encode()).hexdigest()

# Create blocks
genesis_block = Block(0, time.time(), "Genesis Block", "0")
block1 = Block(1, time.time(), "Block 1 Data", genesis_block.hash)
block2 = Block(2, time.time(), "Block 2 Data", block1.hash)

# Link blocks
blockchain = [genesis_block, block1, block2]

# Display blocks
for block in blockchain:
    print(f"Block #{block.index} Hash: {block.hash}")

# Change data of block1 and observe
block1.data = "Tampered Data"
block1.hash = block1.calculate_hash()
print("\nAfter Tampering:")
for block in blockchain:
    print(f"Block #{block.index} Hash: {block.hash}")
