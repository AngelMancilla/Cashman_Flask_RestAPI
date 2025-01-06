from enum import Enum 

class TransactionType(Enum):
    """
    Enum to represent the type of financial transactions.

    Attributes:
        INCOME (str): Represents income transactions.
        EXPENSE (str): Represents expense transactions.
    """
    INCOME = 'income'
    EXPENSE = 'expense'