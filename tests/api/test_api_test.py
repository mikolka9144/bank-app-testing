import requests
import json
from src.account import Account
import pytest

URL = "http://localhost:5000/"
class TestAccount:

    @pytest.fixture(autouse=True)
    def set_up(self):
        ext_account = Account("John","Doe","32111111111")
        ext_account.balance = 100
        assert requests.post(
            URL + "api/accounts",
            data=json.dumps({
                "first_name": ext_account.first_name,
                "last_name": ext_account.last_name,
                "pesel": "32111111111"
            }),
            headers={"Content-Type": "application/json"}
        ).status_code == 201
        assert requests.post(
            URL + "api/accounts",
            data=json.dumps({
                "first_name": "TEst",
                "last_name": "Kowalski",
                "pesel": "32145612323"
            }),
            headers={"Content-Type": "application/json"}
        ).status_code == 201
        assert requests.post(
            URL + "/api/accounts/32145612323/transfer",
            data=json.dumps({
                "amount": "100",
                "type": "incoming"
            }),
            headers={"Content-Type": "application/json"}
        ).status_code == 201
        yield 

        get_req = requests.get(URL+"api/accounts")
        result = [x.get("pesel") for x in json.loads(get_req.content)]
        for y in result:
            assert requests.delete(URL+"/api/accounts/"+y).status_code == 200

    @pytest.fixture()
    def ext_account(self):
        acc = Account("John","Doe","32111111111")
        acc.balance = 100
        return acc

    def test_account_add(self,ext_account):
        post_req = requests.post(
            URL + "api/accounts",
            data=json.dumps({
                "first_name": ext_account.first_name,
                "last_name": ext_account.last_name,
                "pesel": "321"
            }),
            headers={"Content-Type": "application/json"}
        )
        get_req = requests.get(URL+"api/accounts/"+ext_account.pesel)

        assert post_req.status_code == 201
        assert get_req.status_code == 200    
    def test_account_transfer_in(self,ext_account):
        post_req = requests.post(
            URL + "/api/accounts/32145612323/transfer",
            data=json.dumps({
                "amount": "50",
                "type": "incoming"
            }),
            headers={"Content-Type": "application/json"}
        )
        get_req = requests.get(URL+"api/accounts/"+ext_account.pesel)

        assert post_req.status_code == 201
        assert get_req.status_code == 200

    def test_account_transfer_out(self,ext_account):
        post_req = requests.post(
            URL + "/api/accounts/32145612323/transfer",
            data=json.dumps({
                "amount": 50,
                "type": "outgoing"
            }),
            headers={"Content-Type": "application/json"}
        )
        get_req = requests.get(URL+"api/accounts/"+ext_account.pesel)

        assert post_req.status_code == 201
        assert get_req.status_code == 200    
        
    def test_account_transfer_out_outofMoney(self,ext_account):
        post_req = requests.post(
            URL + "/api/accounts/32145612323/transfer",
            data=json.dumps({
                "amount": "5000",
                "type": "outgoing"
            }),
            headers={"Content-Type": "application/json"}
        )

        assert post_req.status_code == 422   
    def test_account_transfer_noAccount(self,ext_account):
        post_req = requests.post(
            URL + "/api/accounts/32145612300/transfer",
            data=json.dumps({
                "amount": "5000",
                "type": "outgoing"
            }),
            headers={"Content-Type": "application/json"}
        )

        assert post_req.status_code == 404

    def test_account_transfer_express(self,ext_account):
        post_req = requests.post(
            URL + "/api/accounts/32145612323/transfer",
            data=json.dumps({
                "amount": "50",
                "type": "express"
            }),
            headers={"Content-Type": "application/json"}
        )
        get_req = requests.post(
            URL + "/api/accounts/32145612323/transfer",
            data=json.dumps({
                "amount": "49",
                "type": "outgoing"
            }),
            headers={"Content-Type": "application/json"}
        )

        assert post_req.status_code == 201
        assert get_req.status_code == 201

    def test_account_add_failOnAlreadyExisting(self,ext_account):
        post_req = requests.post(
            URL + "api/accounts",
            data=json.dumps({
                "first_name": ext_account.first_name,
                "last_name": ext_account.last_name,
                "pesel": "32222222121"
            }),
            headers={"Content-Type": "application/json"}
        )       
        post_req2 = requests.post(
            URL + "api/accounts",
            data=json.dumps({
                "first_name": ext_account.first_name,
                "last_name": ext_account.last_name,
                "pesel": "32222222121"
            }),
            headers={"Content-Type": "application/json"}
        )

        assert post_req.status_code == 201
        assert post_req2.status_code == 409

    def test_account_getAll(self,ext_account):
        
        get_req = requests.get(URL+"api/accounts")
        assert get_req.status_code == 200

        result = json.loads(get_req.content)
        assert result[0].get("name") == ext_account.first_name
        assert result[1].get("name") == "TEst"

    def test_account_count(self,ext_account):
        requests.post(
            URL + "api/accounts",
            data=json.dumps({
                "first_name": ext_account.first_name,
                "last_name": ext_account.last_name,
                "pesel": "321"
            }),
            headers={"Content-Type": "application/json"}
        )
        requests.post(
            URL + "api/accounts",
            data=json.dumps({
                "first_name": "TEst",
                "last_name": "Kowalski",
                "pesel": "321456"
            }),
            headers={"Content-Type": "application/json"}
        )
        get_req = requests.get(URL+"api/accounts")
        assert get_req.status_code == 200

        result = json.loads(get_req.content)
        assert result[0].get("name") == ext_account.first_name
        assert result[1].get("name") == "TEst"