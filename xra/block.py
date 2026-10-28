
import hashlib, time, json

class Block:
    def __init__(self, index, previous_hash, transactions, nonce=0):
        self.index = index
        self.previous_hash = previous_hash
        self.timestamp = time.time()
        self.transactions = transactions
        self.nonce = nonce
        self.hash = self.calculate_hash()

    def calculate_hash(self):
        tx_ids = [t.tx_id if hasattr(t,  tx_id ) else str(t) for t in self.transactions]
        block_string = json.dumps({
            "index": self.index,
            "previous_hash": self.previous_hash,
            "timestamp": self.timestamp,
            "transactions": tx_ids,
            "nonce": self.nonce
        }, sort_keys=True)
        return hashlib.sha256(block_string.encode( utf-8 )).hexdigest()

    def mine_block(self, difficulty):
        target = "0" * difficulty
        while self.hash[:difficulty] != target:
            self.nonce += 1
            self.hash = self.calculate_hash()
        return self.hash

    def to_dict(self):
        return {
            "index": self.index,
            "previous_hash": self.previous_hash,
            "timestamp": self.timestamp,
            "transactions": [t.to_dict() if hasattr(t,  to_dict ) else str(t) for t in self.transactions],
            "nonce": self.nonce,
            "hash": self.hash
        }
