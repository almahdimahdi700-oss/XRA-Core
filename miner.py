
import sys, time, requests

def mine_loop(address):
    print(f"=== XRA Miner for {address} ===")
    url = f"http://localhost:5000/mine/{address}"
    while True:
        try:
            r = requests.get(url, timeout=30)
            data = r.json()
            print(f"MINED {data.get( block_hash )} Balance {data.get( new_balance )} XRA")
        except Exception as e:
            print(f"Waiting for node... {e}")
            time.sleep(5)
        time.sleep(2)

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python miner.py XRAADDRESS")
        sys.exit(1)
    mine_loop(sys.argv[1])
