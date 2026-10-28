
from .block import Block
from .transaction import Transaction

class XRAChain:
    def __init__(self):
        self.name = "XRA"
        self.full_name = "XRA - Abdullah Cross-Border Balance Report"
        self.ticker = "XRA"
        self.chain = [self.create_genesis_block()]
        self.difficulty = 4
        self.pending_transactions = []
        self.mining_reward = 100
        self.max_supply = 21000000

    def create_genesis_block(self):
        genesis_tx = Transaction("GENESIS", "XRA8ABDULLAHGENESIS", 0)
        block = Block(0, "0", [genesis_tx])
        return block

    def get_latest_block(self):
        return self.chain[-1]

    def add_transaction(self, transaction: Transaction):
        if not transaction.sender or not transaction.recipient:
            raise ValueError("Invalid")
        self.pending_transactions.append(transaction)

    def mine_pending(self, miner_address: str):
        reward_tx = Transaction(None, miner_address, self.mining_reward)
        self.pending_transactions.append(reward_tx)
        block = Block(len(self.chain), self.get_latest_block().hash, self.pending_transactions)
        block.mine_block(self.difficulty)
        self.chain.append(block)
        self.pending_transactions = []
        return block

    def get_balance(self, address: str):
        balance = 0
        for block in self.chain:
            for tx in block.transactions:
                if tx.recipient == address:
                    balance += tx.amount
                if tx.sender == address:
                    balance -= tx.amount
        return balance

    def is_valid(self):
        for i in range(1, len(self.chain)):
            curr = self.chain[i]
            prev = self.chain[i-1]
            if curr.hash != curr.calculate_hash():
                return False
            if curr.previous_hash != prev.hash:
                return False
        return True

    def to_dict(self):
        return {
            "name": self.name,
            "ticker": self.ticker,
            "length": len(self.chain),
            "chain": [b.to_dict() for b in self.chain]
        }
