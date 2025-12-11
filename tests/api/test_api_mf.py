from src.account import CompanyAccount
import pytest

class MFTests:

    def test_nip_valid(self):
        acc = Account("John","Doe","32111111111")
        acc.balance = 100
        return acc