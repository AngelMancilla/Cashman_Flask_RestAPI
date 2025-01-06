from marshmallow import post_load
from .transaction import Transaction, TransactionSchema
from .transaction_type import TransactionType

class Income(Transaction):
    """
    Representa una transacción de ingreso, heredada de la clase base Transaction.
    """
    def __init__(self, description, amount):
        if not isinstance(description, str):
            raise ValueError("Description must be a string")
        if not isinstance(amount, (int, float)):
            raise ValueError("Amount must be a number")
        if amount <= 0:
            raise ValueError("Amount must be greater than zero")
        super(Income, self).__init__(description, amount, type=TransactionType.INCOME.value)

    def __repr__(self):
        """
        Representación en forma de string de la instancia Income.
        """
        return f"<Income(description={self.description!r}, amount={self.amount})>"

class IncomeSchema(TransactionSchema):
    """
    Esquema para serializar y deserializar objetos Income usando Marshmallow.
    """
    @post_load
    def make_income(self, data, **kwargs):
        return Income(**data)

