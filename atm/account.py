import typing as ty
from decimal import Decimal
from .exceptions import InsufficientFunds
from .utils import currency

Acct = ty.TypeVar('Acct')

class Account(ty.Generic[Acct]):
    """Base Account Class"""
    def __init__(self, acc_type: str, amount: str):
        self.account_type = acc_type
        self.amount = currency(amount)

    def deposit(self, amount: str) -> Decimal:
        self.amount += currency(amount)
        return self.amount
    
    def withdraw(self, amount: str) -> Decimal:
        amount = currency(amount)

        if amount > self.amount:
            raise InsufficientFunds(f'Funds not available to withdraw {amount}')
        
        self.amount -= amount
        return self.amount
    
    def balance(self) -> Decimal:
        return self.amount
    
    def transfer_funds(self, amount: str, account: Acct) -> Acct:
        amount = currency(amount)
        self.withdraw(amount)
        account.deposit(amount)

        return account


class SavingsAccount(Account):
    """Representation of a Savings Account"""
    def __init__(self, amount):
        super(SavingsAccount, self).__init__('savings', amount)


class CheckingAccount(Account):
    """Representation of a Checking Account"""
    def __init__(self, amount):
        super(CheckingAccount, self).__init__('checking', amount)
    