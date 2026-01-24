from behave import *
import requests, json

URL = "http://localhost:5000"


@step('Account with pesel "{pesel}" has balance equal to "{balance}"')
def check_balance(context, pesel,balance):
    response = requests.get(URL + f"/api/accounts/{pesel}")
    body = response.json()
    assert int(body["balance"]) == int(balance)

@when('I transfer out "{balance}" from account with pesel: "{pesel}"')
def trand_out(context,balance,pesel):
    post_req = requests.post(
        URL + f"/api/accounts/{pesel}/transfer",
        data=json.dumps({
            "amount": f"{balance}",
            "type": "outgoing"
        }),
        headers={"Content-Type": "application/json"}
        )
    assert post_req.status_code == 201 

@when('I fail to transfer out "{balance}" from account with pesel: "{pesel}"')
def trans_fail_out(context,balance,pesel):
    post_req = requests.post(
        URL + f"/api/accounts/{pesel}/transfer",
        data=json.dumps({
            "amount": f"{balance}",
            "type": "outgoing"
        }),
        headers={"Content-Type": "application/json"}
        )
    assert post_req.status_code == 422

@when('I transfer in "{balance}" to account with pesel: "{pesel}"')
def trans_in(context,balance,pesel):
    post_req = requests.post(
        URL + f"/api/accounts/{pesel}/transfer",
        data=json.dumps({
            "amount": f"{balance}",
            "type": "incoming"
        }),
        headers={"Content-Type": "application/json"}
        )
    assert post_req.status_code == 201 