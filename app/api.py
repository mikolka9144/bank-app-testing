from flask import Flask, request, jsonify
from src.accountRegistry import AccountsRegistry
from src.account import Account


app = Flask(__name__)
registry = AccountsRegistry()

@app.route("/api/accounts", methods=['POST'])
def create_account():
    data = request.get_json()
    print(f"Create account request: {data}")
    if registry.account_exists( data["pesel"]):
        return "Account already exists",409
    account = Account(data["first_name"], data["last_name"], data["pesel"])
    registry.add_account(account)
    return jsonify({"message": "Account created"}), 201
    
@app.route("/api/accounts", methods=['GET'])
def get_all_accounts():
    print("Get all accounts request received")
    accounts = registry.get_all_accounts()
    accounts_data = [{"name": acc.first_name, "surname": acc.last_name, "pesel":
    acc.pesel, "balance": acc.balance} for acc in accounts]
    return jsonify(accounts_data), 200

@app.route("/api/accounts/count", methods=['GET'])
def get_account_count():
    print("Get account count request received")
    count = len(registry.accounts)
    return jsonify({"count": count}), 200

@app.route("/api/accounts/<pesel>", methods=['GET'])
def get_account_by_pesel(pesel):
    acc = registry.find_account_by_pesel(pesel)
    if acc is not None:
        return jsonify({"first_name": acc.first_name, "last_name": acc.last_name, "pesel":
        acc.pesel,"balance": acc.balance}), 200
    else:
        return "Error", 404

@app.route("/api/accounts/<pesel>/transfer", methods=['POST'])
def transfer_money(pesel):
    acc = registry.find_account_by_pesel(pesel)
    if acc is None:
        return "No Account found", 404
    data = request.get_json()
    amount = int(data["amount"])
    match data["type"]:
        case "incoming":
            acc.transfer_money(-amount,None)
        case "outgoing":
            if amount > acc.balance:
                return "Not enough money",422
            acc.transfer_money(amount,None)
        case "express":
             acc.express_transfer(amount,None)
        case _:
            return "Invalid action", 400
    return "Done",201
    

@app.route("/api/accounts/<pesel>", methods=['PATCH'])
def update_account(pesel):
    acc = registry.find_account_by_pesel(pesel)
    if acc is not None:
        data = request.get_json()
        if data.first_name is not None:
            acc.first_name = data.first_name        
        if data.last_name is not None:
            acc.last_name = data.last_name
        return jsonify({"message": "Account updated"}), 200
    else:
        return "Error", 404
    #implementacja powinna znaleźć się tutaj
    
@app.route("/api/accounts/<pesel>", methods=['DELETE'])
def delete_account(pesel):
    acc = registry.find_account_by_pesel(pesel)
    if acc is not None:
        registry.accounts.remove(acc)
        return jsonify({"message": "Account deleted"}), 200
    else:
        return "Error", 404


    