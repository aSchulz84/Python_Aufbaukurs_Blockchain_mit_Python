from hashlib import sha256

difficulty = 3


class Block:

    def __init__(self, index, transactions, timestamp, previous_hash):
        self.index = index
        self.transactions = transactions
        self.timestamp = timestamp
        self.previous_hash = previous_hash

        self.nonce = 0

        self.hash = self.calculate_hash()

    def calculate_hash(self):
        string_to_hash = "{0}{1}{2}{3}{4}".format(
            self.index,
            self.transactions,
            self.timestamp,
            self.previous_hash,
            self.nonce
        )
        hash = sha256(string_to_hash.encode("utf-8")).hexdigest()

        while not hash.startswith("6" * difficulty):

            self.nonce += 1
            string_to_hash = "{0}{1}{2}{3}{4}".format(
                self.index,
                self.transactions,
                self.timestamp,
                self.previous_hash,
                self.nonce
            )

            hash = sha256(string_to_hash.encode("utf-8")).hexdigest()
        return hash
