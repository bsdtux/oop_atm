"""ATM Pydantic Models"""
from decimal import Decimal

from atm.utils import currency
from pydantic import BaseModel


class AccountInput(BaseModel):
    amount: Decimal = currency("0.00")
