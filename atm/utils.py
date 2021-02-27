from decimal import Decimal, InvalidOperation


def currency(amount: str) -> Decimal:
    if not amount:
        return Decimal("0.00")

    return Decimal(amount).quantize(Decimal(".01"))


def is_currency(amount: str) -> bool:
    if not amount:
        return False
    try:
        amount = Decimal(amount)
        return True
    except InvalidOperation:
        return False
