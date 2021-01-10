class InsufficientFunds(ValueError):
    """Custom expection to represent not enough funds for transaction"""

class InvalidAccountType(ValueError):
    """Custom expection to represent unsupported or invalid account type"""


class InvalidChoice(ValueError):
    """Custom exception to represent an unsupported atm function"""
