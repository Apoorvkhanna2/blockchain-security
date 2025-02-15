import hashlib
import time

# Simple User Authentication
users = {"admin": "apoorv123"}  # User database

def login():
    username = input("Enter username: ")
    password = input("Enter password: ")

    if users.get(username) == password:
        print("\n✅ Login successful!\n")
        return True
    else:
        print("\n❌ Invalid credentials! Access Denied.\n")
        return False

class Blockchain:
    def __init__(self):
        self.chain = []
        self.create_block(proof=1, previous_hash="0")

    def create_block(self, proof, previous_hash):
        block = {
            'index': len(self.chain) + 1,
            'timestamp': time.time(),
            'proof': proof,
            'previous_hash': previous_hash
        }
        self.chain.append(block)
        return block

    def get_previous_block(self):
        return self.chain[-1]

    def proof_of_work(self, previous_proof):
        new_proof = 1
        while True:
            hash_operation = hashlib.sha256(str(new_proof**2 - previous_proof**2).encode()).hexdigest()
            if hash_operation[:4] == "0000":
                return new_proof
            new_proof += 1

    def hash(self, block):
        return hashlib.sha256(str(block).encode()).hexdigest()

    def print_chain(self):
        for block in self.chain:
            print(f"\n🔹 Block {block['index']}")
            print(f"   Timestamp: {block['timestamp']}")
            print(f"   Proof: {block['proof']}")
            print(f"   Previous Hash: {block['previous_hash']}")

# Run only if login is successful
if login():
    blockchain = Blockchain()

    while True:
        print("\n1️⃣ Mine Block  |  2️⃣ View Blockchain  |  3️⃣ Exit")
        choice = input("Choose an option: ")

        if choice == "1":
            previous_block = blockchain.get_previous_block()
            proof = blockchain.proof_of_work(previous_block['proof'])
            previous_hash = blockchain.hash(previous_block)
            new_block = blockchain.create_block(proof, previous_hash)
            print("\n✅ Block Mined!")
            print(f"🔹 Block Index: {new_block['index']}")
        elif choice == "2":
            blockchain.print_chain()
        elif choice == "3":
            print("\n🚀 Exiting Blockchain...")
            break
        else:
            print("\n❌ Invalid choice! Try again.")
