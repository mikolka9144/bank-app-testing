import os
import requests
import json
import datetime
from src.account import BaseAccount

class CompanyAccount(BaseAccount):
        def __init__(self, company_name, nip_number):
            super().__init__()
            self.company_name = company_name
            if(len(nip_number) != 10):
                self.nip_number = "Invalid"
            elif(self.is_nip_valid(nip_number)):
                self.nip_number = nip_number
            else:
                raise ValueError("Company not registered!!")
        def is_nip_valid(self,nip) -> bool:
            urlRoot = os.getenv("BANK_APP_MF_URL","https://wl-test.mf.gov.pl")
            date = datetime.date.today().strftime("%Y-%m-%d")
            response = requests.get(f"{urlRoot}/api/search/nip/{nip}?{date}")
            print("Made a request!")
            if response.status_code == 200:
                return load(response.content).result.subject.statusVat == "Czynny"
            else:
                return False
        def express_transfer(self,amount,recipient_account):
            super().express_transfer(amount,recipient_account,5)
        def take_loan(self,amount):
            con = self.balance*2>amount and (-1775 in self.history)
            if con:
                self.balance += amount
            return con