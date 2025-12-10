from src.account import Account

class AccountsRegistry:
    def __init__(self):
        self.accounts = []

    def add_account(self, new_account):
        self.accounts.append(new_account)
    def account_exists(self,pesel):
        for x in self.accounts:
            if x.pesel == pesel:
                return True
        return False

    def find_account_by_pesel(self, pesel) -> Account:
        for account in self.accounts:
            if account.pesel == pesel:
                return account
        return None  

    def get_all_accounts(self):
        return self.accounts

    def count_accounts(self):
        return len(self.accounts)