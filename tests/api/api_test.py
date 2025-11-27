import requests
import json
from src.account import Account
import pytest

URL = "http://localhost:5000/"
class TestAccount:

    @pytest.fixture
    def set_up(self):
        self.ext_account = Account("John","Doe","321")
        self.ext_account.balance = 100
        requests.post(
            URL + "api/accounts",
            data=json.dumps({
                "first_name": self.ext_account.first_name,
                "last_name": self.ext_account.last_name,
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
        yield
        get_req = requests.get(URL+"api/accounts")
        result = json.loads(get_req.content)

    @pytest.fixture
    def ext_account(self):
        
        return self.ext_account

    def test_account_add(self):
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
        result = json.loads(get_req.content)
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