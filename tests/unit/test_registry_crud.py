from src.accountRegistry import AccountsRegistry
from src.account import Account
import pytest

class TestRegistry:

    @pytest.fixture(autouse=True)
    def setup_method(self):
        self.registry = AccountsRegistry()
        self.account1 = Account("John", "Doe", pesel='12345678901')
        self.account2 = Account("John", "Dog", pesel='10987654321')

    def test_add_account(self):
        self.registry.add_account(self.account1)
        assert len(self.registry.get_all_accounts()) == 1

    def test_find_account_by_pesel_found(self):
        self.registry.add_account(self.account1)
        found_account = self.registry.find_account_by_pesel('12345678901')
        assert found_account == self.account1

    def test_find_account_by_pesel_not_found(self):
        self.registry.add_account(self.account1)
        found_account = self.registry.find_account_by_pesel('00000000000')
        assert found_account is None

    def test_count_accounts(self):
        self.registry.add_account(self.account1)
        self.registry.add_account(self.account2)
        assert self.registry.count_accounts() == 2

    def test_get_all_accounts(self):
        self.registry.add_account(self.account1)
        self.registry.add_account(self.account2)
        assert self.account1 in self.registry.get_all_accounts()
        assert self.account2 in self.registry.get_all_accounts()
        assert len(self.registry.get_all_accounts()) == 2
