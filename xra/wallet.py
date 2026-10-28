
import hashlib
import ecdsa

class Wallet:
    def __init__(self):
        self.private_key = ecdsa.SigningKey.generate(curve=ecdsa.SECP256k1)
        self.public_key = self.private_key.get_verifying_key()
        self.address = self.generate_address()

    def generate_address(self):
        public_bytes = self.public_key.to_string()
        sha = hashlib.sha256(public_bytes).digest()
        ripe = hashlib.new( ripemd160 , sha).hexdigest()
        return "XRA" + ripe[:30].upper()

    def get_keys_hex(self):
        return {
            "private_key": self.private_key.to_string().hex(),
            "public_key": self.public_key.to_string().hex(),
            "address": self.address
        }
