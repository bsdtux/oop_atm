from .account import SavingsAccount, CheckingAccount
from .exceptions import InvalidAccountType, InvalidChoice, InsufficientFunds
from .utils import is_currency


class ATM:
    def __init__(self):
        self.accounts = []
    
    def menu(self):
        self._print_header()
        print(" " * 4 + "1. Show Balance")
        print(" " * 4 + "2. Deposit")
        print(" " * 4 + "3. Withdraw")
        print(" " * 4 + "4. Transfer Funds")
        print(" " * 4 + "5. Add Account")
        print(" " * 4 + "6. Quit")
    
    def choice(self, choice: int):
        choice_map = {1: self.show_balance, 2: self.deposit, 3: self.withdraw, 4: self.transfer_funds, 5: self.add_account}

        func = choice_map.get(choice) or None

        if not func:
            raise InvalidChoice(f'Option selected {choice} is not a valid option.')
        func()

    def add_account(self):
        account_types = {1: CheckingAccount, 2: SavingsAccount}

        while True:
            try:
                choice = int(input('Select account type (1. checking, 2. savings) >>>> '))
                print(f'ADD ACCOUNT: {choice}')
                if choice not in account_types:
                    raise InvalidChoice("Invalid Account selection please try again.")
            except (ValueError, InvalidChoice) as exc_info:
                print(str(exc_info))
                continue

            break
            
        starting_balance = self._get_currency_amount('Enter your starting balance >>>> ')
        
        new_account = account_types[choice](starting_balance)
        self.accounts.append(new_account)
        return new_account

    def show_balance(self):
        if not self.accounts:
            return self._no_account_message()
        account = self._get_account()
        print(f'\nAccount Balance: >>> {account.balance()}\n')

    def deposit(self):
        if not self.accounts:
            return self._no_account_message()

        to_acct = self._get_account()
        to_acct.deposit(
            self._get_currency_amount('Enter the amount you would like to deposit >>>> ')
        )  

    def withdraw(self):
        if not self.accounts:
            return self._no_account_message()
        
        from_acct = self._get_account()

        try:
            from_acct.withdraw(
                self._get_currency_amount('Enter withdraw amount >>>> ')
            )
        except(ValueError, InsufficientFunds) as exc_info:
            print(str(exc_info))

    def transfer_funds(self):
        if not self.accounts:
            return self._no_account_message()
        
        from_acct = self._get_account()
        to_acct = self._get_account()

        from_acct.transfer_funds(
            self._get_currency_amount('How much would you like to transfer >>> '),
            to_acct
        )

    def _get_account(self):
        if not self.accounts:
            return self._no_account_message()
        
        account = None
        while not account:
            self._list_accounts()

            try:
                choice = int(input('Select account >>>> '))
                if choice-1 > len(self.accounts):
                    raise InvalidChoice("Invalid Account selection please try again.")

                return self.accounts[choice - 1]
            except (ValueError, InvalidChoice) as exc_info:
                print(str(exc_info))
                continue
    
    def _no_account_message(self):
        print('\nNo accounts were found. Please setup an account first\n')
        return None

    def _list_accounts(self):
        for i, acct in enumerate(self.accounts):
            print(' ' * 4 + f'{i + 1}. {acct.account_type}\n')    

    def _get_currency_amount(self, message = 'Enter an amount >>> '):
        amount = ''
        while True:
            amount = input(message)
            if not is_currency(amount):
                print("Not a valid currency format. Must be in the format of 0.00\n")
                continue

            break
        return amount
    
    def _print_header(self):
        print("=" * 10 + " Bank Co ATM " + "=" * 10)