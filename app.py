import datetime
from flask import Flask, render_template, request
from hashlib import sha256

from block import Block
from orders import Orders
from smartcontract import SmartContract
from users import User
from users import Company

smart_contract = SmartContract()

app = Flask(__name__)

blockchain = []

transactions = []

customer1 = User(
    "Petra", 100, 0, sha256("Petra".encode("utf-8")).hexdigest())

company = Company("FAST Logistics", 899112985000,
                  sha256("FAST Logistics".encode("utf-8")).hexdigest())

blockchain.append(Block(0, [], datetime.datetime.now(), "GENESIS",))


@app.route("/")
def index():
    return render_template("index.html", name=customer1.name)


@app.route("/index.html")
def index2():

    return render_template("index.html", name=customer1.name)


@app.route("/order.html", methods=["GET", "POST"])
def auftrag():

    global transaction
    global fee1
    if request.method == "POST":

        type = request.form["type"]
        weight = request.form["weight"]
        sender = customer1.name
        receiver = request.form["receiver"]
        destination = request.form["destination"]
        transaction = Orders(type, weight, sender, receiver,
                             destination, customer1.wallet, company.wallet)
        smart_contract.cargo_properities(transaction)
        fee1 = "Die Gebühr hierfür beträgt 1 FAST Token."

        if transaction.everything_fine == True:
            transactions.append(transaction)
            order3 = "Ihre Eingabe war erfolgreich!"
            order3_1 = "Sie können nun weitere Aufträge aufgeben oder Ihren Auftrag an die Blockchain übermitteln."
            fee1 = "Die Gebühr hierfür beträgt 1 FAST Token."
            customer1.orders += 1
            return render_template("order.html", order3=order3, order3_1=order3_1, fee1=fee1)
        else:
            order2 = "Die Eingabe war leider nicht erfolgreich."
            order2_1 = "Ihre Fracht-Eigenschaften entsprechen nicht Ihren Vertragsbedingugnen. Bitte überprüfen Sie Ihre Angaben und führen Sie den Auftrag ggfs. erneut aus."
            return render_template("order.html", order2=order2, order2_1=order2_1)
    else:
        return render_template("order.html")


@app.route("/mine.html")
def mine():
    global blockchain
    global transactions

    if len(transactions) <= 0:
        mining1 = "Leider nicht erfolgreich"
        mining2 = "Keine offenen Aufträge"
        return render_template("mine.html", mining2=mining2, mining1=mining1)
    else:
        mining3 = "Erfolgreiche Übermittlung!"
        customer1.coins -= 1
        company.coins += 1
        blockchain.append(Block(len(blockchain), transactions,
                                datetime.datetime.now(), blockchain[-1].hash,))
        transactions_temp = transactions
        transactions = []
        return render_template("mine.html", mining=len(transactions_temp), fee1=fee1, mining3=mining3)


@app.route("/blockchain.html")
def blockchain_site():
    return render_template("blockchain.html", blockchain=blockchain)


@app.route("/account.html")
def account():
    return render_template("account.html", customer1=customer1)


@app.route("/fast_wallet.html")
def fast_wallet():
    amount = f"{company.coins:,}"
    return render_template("fast_wallet.html", amount=amount, address=company.wallet)


app.run(debug=True)
