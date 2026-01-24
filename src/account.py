import math
import requests
import datetime
import os
from typing import Any
from smtp.smtp import SMTPClient

class BaseAccount:
    def __init__(self):
        self.balance = 0
        self.history = []
    def transfer_money(self, amount, recipient_account):
        if amount <= self.balance:
            self.balance -= amount
            self.history.append(-amount)
            if recipient_account is not None:
                recipient_account.balance += amount
                recipient_account.history.append(amount)
    def express_transfer(self,amount,recipient_account,provision = 0):
        if amount > self.balance:
            return
        self.transfer_money(amount,recipient_account)
        self.balance -= provision
        self.history.append(-provision)
    def send_history_via_email(self,email_address,account_type):
        return SMTPClient.send("Account Transfer History "+str(datetime.date.today()),account_type+" account history: "+str(self.history),email_address)
    def to_dict(self) -> dict[str, Any]:
        return {
            "balance":self.balance,
            "history":self.history
        }
    def from_dict(dict):
            obj = BaseAccount()
            obj.history = dict["history"]
            obj.balance = dict["balance"]
            return obj

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
    def send_history_via_email(self,email_address):
        return super().send_history_via_email(email_address,"Personal")
    def to_dict(self) -> dict[str, Any]:
        return {
            "first_name":self.first_name,
            "last_name":self.last_name,
            "pesel":self.pesel,
            "balance":self.balance,
            "history":self.history
        }
    def from_dict(dict):
        obj = Account(dict["first_name"],dict["last_name"],dict["pesel"])
        obj.history = dict["history"]
        obj.balance = dict["balance"]
        return obj

