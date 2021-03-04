"""ATM Account Representation Module"""
from dataclasses import dataclass
from decimal import Decimal

from .utils import currency


@dataclass
class Account:
    id: int = 0
    description: str = ""
    amount: currency = currency(0.00)


@dataclass
class Savings(Account):
    description: str = "Savings"


@dataclass
class Checking(Account):
    description: str = "Checking"


mock_records = {
    1: Savings(id=1, amount=currency("1000.00")),
    2: Checking(id=2, amount=currency("1000.00")),
    3: Checking(id=3, amount=currency("750.00")),
}


class Model:
    def __init__(self):
        self.database = mock_records

    def get_account_by_id(self, account_id):
        return mock_records.get(account_id)

    def get_accounts(self):
        return self.database

    def update_account(self, account_id, account):
        mock_records[account_id] = account
