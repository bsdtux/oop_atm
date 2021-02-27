from .account import Model
from .exceptions import InsufficientFunds, NoAccountFound
from .utils import currency


class AtmController:
    def __init__(self):
        self.model = Model()

    def deposit(self, account_id: int, amount: str):
        account = self._get_account_or_raise(account_id)
        account.amount += currency(amount)
        self.model.update_account(account_id, account)

        return account

    def withdraw(self, account_id: int, amount: str):
        account = self._get_account_or_raise(account_id)

        amount = currency(amount)
        if account.amount - amount <= 0:
            raise InsufficientFunds(f"Not enough funds to withdraw: {amount}")

        account.amount -= amount
        self.model.update_account(account_id, account)

        return account

    def get_account(self, account_id):
        account = self._get_account_or_raise(account_id)
        return account

    def get_accounts(self):
        return self.model.get_accounts()

    def _get_account_or_raise(self, account_id):
        account = self.model.get_account_by_id(account_id)

        if not account:
            raise NoAccountFound(f"No account matching id: {account_id} was found")

        return account
