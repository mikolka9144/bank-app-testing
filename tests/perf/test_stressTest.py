import requests
import json
from src.account import Account
import pytest

URL = "http://localhost:5000/"
class TestServerLoad:
    
    @pytest.fixture()
    def ext_account(self):
        acc = Account("John","Doe","32111111111")
        acc.balance = 100
        return acc

    def test_account_add_load(self,ext_account):
        for x in range(100): 
            post_req = requests.post(
                URL + "api/accounts",
                data=json.dumps({
                    "first_name": ext_account.first_name,
                    "last_name": ext_account.last_name,
                    "pesel": ext_account.pesel
                }),
                headers={"Content-Type": "application/json"},
                timeout=0.5
            )
            get_req = requests.delete(URL+"api/accounts/"+ext_account.pesel,timeout=0.5)

            assert post_req.status_code == 201
            assert get_req.status_code == 200       
    def test_account_balance(self,ext_account):
        requests.delete(URL+"api/accounts/"+ext_account.pesel,timeout=0.5)
        post_req = requests.post(
            URL + "api/accounts",
            data=json.dumps({
                "first_name": ext_account.first_name,
                "last_name": ext_account.last_name,
                "pesel": ext_account.pesel
            }),
            headers={"Content-Type": "application/json"},
            timeout=0.5
        )
        assert post_req.status_code == 201
        for x in range(100): 
            post_req = requests.post(
            URL + "/api/accounts/"+ext_account.pesel+"/transfer",
            data=json.dumps({
                "amount": "50",
                "type": "incoming"
            }),
            headers={"Content-Type": "application/json"},
            timeout=0.5
            )
            assert post_req.status_code == 201   
            
        get_req = requests.get(URL+"api/accounts/"+ext_account.pesel)
        result = json.loads(get_req.content)
        assert result.get("first_name") == ext_account.first_name
        assert result.get("balance") == 100*50