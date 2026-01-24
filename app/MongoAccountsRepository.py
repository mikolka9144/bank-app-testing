from src.accountRegistry import AccountsRegistry, Account
from app.companyAccount import CompanyAccount
from src.account import BaseAccount
import pymongo
class MongoAccountsRepository:
    def __init__(self,repo:AccountsRegistry):
        self.client = pymongo.MongoClient("127.0.0.1")
        self.repo = repo
        self.remote_repo = self.client["accounts"]
        self._collection = self.remote_repo.get_collection("account_blobs")
        pass
    def save_all(self):
        self._collection.delete_many({})
        for account in self.repo.accounts:
            self._collection.update_one(
                {"pesel": account.pesel},
                {"$set": account.to_dict()},
                upsert=True)
    def load_all(self):
        self.repo.accounts.clear()
        for doc in self._collection.find():
            if "first_name" in doc.keys():
                self.repo.accounts.append(Account.from_dict(doc))
            elif "nip_number" in doc.keys():
                self.repo.accounts.append(CompanyAccount.from_dict(doc))
            else:
                self.repo.accounts.append(BaseAccount.from_dict(doc))