cargo_types = ["1A", "1B", "1C", "2A", "2B", "2C", "3A", "3B", "3C"]
weight_max = "5325"
legal_destinations = ["USA", "CANADA", "EUROPE", "GREAT BRITAIN"]


class SmartContract:

    def cargo_properities(self, current_transaction):

        if current_transaction.type.upper() in cargo_types and current_transaction.weight <= weight_max and current_transaction.destination.upper() in legal_destinations:
            current_transaction.everything_fine = True
        else:
            current_transaction.everything_fine = False
