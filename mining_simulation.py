import hashlib
import time

class Block:
    def __init__(self, index, data, previous_hash=''):
        self.index = index
        self.timestamp = time.time()
        self.data = data
        self.previous_hash = previous_hash
        self.nonce = 0
        self.hash = self.calculate_hash()

    def calculate_hash(self):
        return hashlib.sha256(f"{self.index}{self.timestamp}{self.data}{self.previous_hash}{self.nonce}".encode()).hexdigest()

    def mine_block(self, difficulty):
        print("Mining block...")
        start_time = time.time()
        target = "0" * difficulty
        while self.hash[:difficulty] != target:
            self.nonce += 1
            self.hash = self.calculate_hash()
        end_time = time.time()
        print(f"Block mined with nonce: {self.nonce}")
        print(f"Hash: {self.hash}")
        print(f"Time taken: {end_time - start_time:.2f} seconds")

# Example
block = Block(1, "Mining Test")
block.mine_block(4)
