import math

class BaseAccount:
    def __init__(self):
        self.balance = 0
        self.history = []
    def transfer_money(self, amount, recipient_account):
        if amount <= self.balance:
            self.balance -= amount
            recipient_account.balance += amount
            self.history.append(-amount)
            recipient_account.history.append(amount)
    def express_transfer(self,amount,recipient_account,provision = 0):
        if amount > self.balance:
            return
        self.transfer_money(amount,recipient_account)
        self.balance -= provision
        self.history.append(-provision)



class Account(BaseAccount):
    def __init__(self, first_name, last_name,pesel,promo_code=None):
        super().__init__()
        self.first_name = first_name
        self.last_name = last_name
        self.balance = 0
        if pesel != None and len(pesel) != 11:
            self.pesel = "Invalid"
        else:
            self.pesel = pesel
            if promo_code != None and promo_code.startswith("PROM_") and len(promo_code) == 8 and self.get_age() < 65:
                self.balance += 50
                self.history.append(50)
    def get_age(self):
        current_year = 2025 # update this every year pls :)
        year = int(self.pesel[:2])
        if(year > 30):
            year = 1900 + year
        else:
            year = 2000 + year
        return current_year - year
    def express_transfer(self,amount,recipient_account):
        super().express_transfer(amount,recipient_account,1)
    def submit_for_loan(self,amount):
        con1 = len(self.history) >= 3 and self.history[-1] > 0  and self.history[-2] > 0  and self.history[-3] > 0
        con2 = len(self.history)>=5 and sum(self.history[-5:]) > amount;
        if con1 or con2:
            self.balance += amount
        return con1 or con2
    def toJson(self):
        return json.dumps(self, default=lambda o: o.__dict__)
    
class CompanyAccount(BaseAccount):
        def __init__(self, company_name, nip_number):
            super().__init__()
            self.company_name = company_name
            if(len(nip_number) != 10):
                self.nip_number = "Invalid"
            else:
                self.nip_number = nip_number
        def express_transfer(self,amount,recipient_account):
            super().express_transfer(amount,recipient_account,5)
        def take_loan(self,amount):
            con = self.balance*2>amount and (-1775 in self.history)
            if con:
                self.balance += amount
            return con
