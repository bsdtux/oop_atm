from decimal import Decimal
from atm.utils import currency, is_currency

def test_currency():
    assert currency('') == Decimal('0.00')
    assert currency(1) == Decimal('1.00')
    assert currency(1.01) == Decimal('1.01')
    assert currency('2.00') == Decimal('2.00')


def test_is_currency():
    assert is_currency('1')
    assert is_currency('.01')
    assert is_currency(1000.00)
    assert not is_currency('a')
    assert not is_currency('')