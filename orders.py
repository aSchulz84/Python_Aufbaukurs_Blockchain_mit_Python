import datetime


class Orders:
    def __init__(self, type, weight, sender, receiver, destination, sender_wallet, receiver_wallet):

        self.type = type
        self.weight = weight
        self.sender = sender
        self.receiver = receiver
        self.destination = destination
        self.sender_wallet = sender_wallet
        self.receiver_wallet = receiver_wallet
        self.time = datetime.datetime.now()
        self.everything_fine = False
