import pytest
from decimal import Decimal
from mock import patch, MagicMock
from atm import ATM, InvalidChoice


@patch('atm.print')
def test_atm_header(print_mock):
    atm = ATM()
    atm._print_header()

    print_mock.assert_called_once()

@patch('atm.print')
def test_no_account_message(print_mock):
    atm = ATM()
    atm._no_account_message()

    print_mock.assert_called_once()

@patch('atm.print')
def test_list_accounts(print_mock, build_account):
    atm = ATM()
    atm.accounts.append(build_account())
    atm._list_accounts()

    assert print_mock.call_count == len(atm.accounts)

@patch('atm.input')
@patch('atm.print')
def test_get_currency_amount(print_mock, input_mock):
    input_mock.side_effect = ['A', '1000']
    atm = ATM()
    result = atm._get_currency_amount()

    assert result == '1000'
    print_mock.assert_called_once()


@patch('atm.input')
@patch('atm.print')
def test_get_account(print_mock, input_mock, build_account):
    input_mock.sid_effect = ['5', '1']
    atm = ATM()
    account = build_account()
    atm.accounts.append(account)

    assert atm._get_account() == account


@patch('atm.print')
def test_atm_menu(print_mock):
    atm = ATM()
    atm.menu()

    assert print_mock.call_count > 2


@patch('atm.ATM.show_balance')
def test_choice(sb_mock):
    atm = ATM()
    atm.choice(1)
    sb_mock.assert_called_once()

    with pytest.raises(InvalidChoice):
        assert atm.choice(99)


@patch('atm.print')
@patch('atm.input')
def test_add_account(input_mock, print_mock):
    input_mock.side_effect = ['3', '1', '1000.00']
    atm = ATM()

    account = atm.add_account()

    assert print_mock.call_count > 2
    assert account.amount == Decimal('1000.00')


@patch('atm.input')
@patch('atm.print')
def test_show_balance(print_mock, input_mock, build_account):
    input_mock.side_effect = ['1']

    atm = ATM()
    assert atm.show_balance() is None

    atm.accounts.append(build_account())
    atm.show_balance()

    assert print_mock.call_count > 1


@patch('atm.input')
@patch('atm.print')
def test_deposit(print_mock, input_mock, build_account):

    input_mock.side_effect = ['1', '500.00']

    atm = ATM()
    assert atm.deposit() is None

    atm.accounts.append(build_account())
    atm.deposit()

    assert atm.accounts[0].amount == Decimal('1700.00')


@patch('atm.input')
@patch('atm.print')
def test_withdraw(print_mock, input_mock, build_account):
    input_mock.side_effect = ['1', '500.00']

    atm = ATM()
    assert atm.withdraw() is None

    atm.accounts.append(build_account())
    atm.withdraw()
    assert atm.accounts[0].amount == Decimal('700.00')


@patch('atm.input')
@patch('atm.print')
def test_transfer(print_mock, input_mock, build_account):
    input_mock.side_effect = ['1', '2', '500.00']

    acct1 = build_account(acc_type='Fake Account 1')
    acct2 = build_account(acc_type='Fake Account 2')

    atm = ATM()
    assert atm.transfer_funds() is None

    atm.accounts.extend([acct1, acct2])
    atm.transfer_funds()
    assert atm.accounts[0].amount == Decimal('700.00')
    assert atm.accounts[1].amount == Decimal('1700.00')