import json
import random
import time
from datetime import datetime

def generate_transaction():
    return {
        "transaction_id": random.randint(100000, 999999),
        "user_id": random.randint(1, 1000),
        "amount": round(random.uniform(10, 10000), 2),
        "merchant": random.choice(["Amazon", "Walmart", "Target", "BestBuy"]),
        "country": random.choice(["US", "IN", "UK", "CA"]),
        "timestamp": datetime.utcnow().isoformat()
    }

if __name__ == "__main__":
    while True:
        txn = generate_transaction()
        print(json.dumps(txn))
        time.sleep(1)
