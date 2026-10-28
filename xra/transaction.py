import hashlib, time

class Transaction:
    def __init__(self, sender, recipient, amount, signature=None):
        self.sender = sender
        self.recipient = recipient
        self.amount = amount
        self.timestamp = time.time()
        self.signature = signature
        self.tx_id = self.calculate_hash()

    def calculate_hash(self):
        data = f"{self.sender}{self.recipient}{self.amount}{self.timestamp}"
        return hashlib.sha256(data.encode( utf-8 )).hexdigest()

    def to_dict(self):
        return {
            "tx_id": self.tx_id,
            "sender": self.sender,
            "recipient": self.recipient,
            "amount": self.amount,
            "timestamp": self.timestamp
        }
