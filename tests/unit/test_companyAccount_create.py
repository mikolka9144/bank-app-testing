from src.account import CompanyAccount
import pytest

class TestCompanyAccount:
    def test_create_company_account(self):
        testificate = CompanyAccount("Test Company","1234567890")
        assert testificate.company_name == "Test Company"
        assert testificate.nip_number == "1234567890"
    def test_invalid_company_account(self):
        testificate = CompanyAccount("Test Company","1234590")
        assert testificate.company_name == "Test Company"
        assert testificate.nip_number == "Invalid"
    def test_invalid_company_nip_account(self,mocker):
        mocker.patch("src.account.CompanyAccount.is_nip_valid", return_value=False)
        with pytest.raises(ValueError):
            testificate = CompanyAccount("Test Company","1234567890")

        

    def test_company_money_transfer(self,mocker):
        mocker.patch("src.account.CompanyAccount.is_nip_valid", return_value=True)
        target = CompanyAccount("Test Company","1234590")
        target.balance = 100
        testificate = CompanyAccount("Test Company","1234590")
        testificate.balance = 100

        testificate.express_transfer(40,target)

        assert testificate.balance == 55
        assert target.balance == 140
    def test_company_money_minus_transfer(self):
        target = CompanyAccount("Test Company","1234590")
        target.balance = 100
        testificate = CompanyAccount("Test Company","1234590")
        testificate.balance = 40

        testificate.express_transfer(40,target)

        assert testificate.balance == -5
        assert target.balance == 140
    def test_company_money_insufficient_transfer(self):
        target = CompanyAccount("Test Company","1234590")
        target.balance = 100
        testificate = CompanyAccount("Test Company","1234590")
        testificate.balance = 40

        testificate.express_transfer(40000,target)

        assert testificate.balance == 40
        assert target.balance == 100
        
        