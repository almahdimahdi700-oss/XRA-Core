from flask import Flask, jsonify, request
from xra.blockchain import XRAChain
from xra.wallet import Wallet
from xra.transaction import Transaction

app = Flask(__name__)
xra_chain = XRAChain()

@app.route('/')
def index():
    return jsonify({
        "name": "XRA Core",
        "ticker": "XRA",
        "meaning": "X=Cross-Border Non-National Crypto, RA=Report Abdullah Balances",
        "website": "https://rgalmahdi.blogspot.com",
        "creator": "Abdullah - رق المهدي",
        "chain_length": len(xra_chain.chain),
        "endpoints": ["/wallet/new", "/balance/<address>", "/transactions/new", "/mine/<address>", "/chain"]
    })

@app.route('/wallet/new', methods=['GET'])
def new_wallet():
    w = Wallet()
    return jsonify(w.get_keys_hex())

@app.route('/balance/<address>', methods=['GET'])
def balance(address):
    bal = xra_chain.get_balance(address)
    return jsonify({"address": address, "balance": bal, "ticker": "XRA"})

@app.route('/transactions/new', methods=['POST'])
def new_transaction():
    data = request.get_json()
    tx = Transaction(data['sender'], data['recipient'], float(data['amount']))
    xra_chain.add_transaction(tx)
    return jsonify({"message": "XRA Transaction added", "tx_id": tx.tx_id}), 201

@app.route('/mine/<miner_address>', methods=['GET'])
def mine(miner_address):
    block = xra_chain.mine_pending(miner_address)
    return jsonify({
        "message": f"Mined {xra_chain.mining_reward} XRA",
        "block_hash": block.hash,
        "new_balance": xra_chain.get_balance(miner_address)
    })

@app.route('/chain', methods=['GET'])
def full_chain():
    return jsonify(xra_chain.to_dict())

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
