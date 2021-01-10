import pytest
from decimal import Decimal
from atm.account import CheckingAccount, SavingsAccount
from atm.exceptions import InsufficientFunds

def test_checking_account():
    acct = CheckingAccount('1200.00')

    assert acct.account_type == 'checking'
    assert acct.balance() == Decimal('1200.00')
    assert acct.deposit('1000.00') == Decimal('2200.00')
    assert acct.withdraw('100') == Decimal('2100.00')

    acct2 = acct.transfer_funds('1000.00', CheckingAccount('0.00'))
    assert acct2.balance() == Decimal('1000.00')

    with pytest.raises(InsufficientFunds) as exc_info:
        assert acct.withdraw('10000.00')


def test_savings_account():
    acct = SavingsAccount('1200.00')
    
    assert acct.account_type == 'savings'
    assert acct.balance() == Decimal('1200.00')
    assert acct.deposit('1000.00') == Decimal('2200.00')
    assert acct.withdraw('100') == Decimal('2100.00')

    acct2 = acct.transfer_funds('1000.00', SavingsAccount('0.00'))
    assert acct2.balance() == Decimal('1000.00')

    with pytest.raises(InsufficientFunds) as exc_info:
        assert acct.withdraw('10000.00')