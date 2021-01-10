import pytest
from functools import partial
from atm.account import Account

@pytest.fixture
def build_account():
    defaults = dict(
        acc_type='Fake Account',
        amount='1200.00'
    )
    return partial(Account, **defaults)
