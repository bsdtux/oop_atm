from atm.controller import AtmController
from atm.utils import is_currency

from .exceptions import InvalidSelection


class ATM:
    quit = 4

    def __init__(self):
        self.api = AtmController()

    def menu(self):
        self._print_header()
        print(" " * 4 + "1. Show Balance")
        print(" " * 4 + "2. Deposit")
        print(" " * 4 + "3. Withdraw")
        print(" " * 4 + "4. Quit")

    def choice(self, choice: int):
        choice_map = {1: self.show_balance, 2: self.deposit, 3: self.withdraw}

        func = choice_map.get(choice) or None

        if not func:
            raise InvalidSelection(f"Option selected {choice} is not a valid option.")
        func()

    def show_balance(self):
        account = self._get_accounts()
        self._display_results(self.api.get_account(account))

    def deposit(self):
        account = self._get_accounts()
        amount = self._get_currency_amount()
        self._display_results(self.api.deposit(account, amount))

    def withdraw(self):
        account = self._get_accounts()
        amount = self._get_currency_amount()
        self._display_results(self.api.withdraw(account, amount))

    def _get_accounts(self):
        self._display_accounts()

        while True:
            try:
                return int(input("Account ID selection: "))
            except InvalidSelection:
                print("Invalid selection please select from a list of accounts above")
                self._display_accounts()

    def _get_currency_amount(self, message="Enter an amount >>> "):
        amount = ""
        while True:
            amount = input(message)
            if not is_currency(amount):
                print("Not a valid currency format. Must be in the format of 0.00\n")
                continue

            break
        return amount

    def _display_accounts(self):
        accounts = self.api.get_accounts()
        for _, (k, v) in enumerate(accounts.items()):
            print(f"Account Number: {k} - {v.description}")

    def _display_results(self, account):
        print(f"Account ID: {account.id} Balance: {account.amount}")

    def _print_header(self):
        print("=" * 10 + " Bank Co ATM " + "=" * 10)
