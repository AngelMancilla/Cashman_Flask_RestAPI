from marshmallow import post_load
from .transaction import Transaction, TransactionSchema
from .transaction_type import TransactionType

class Expense(Transaction):
    """
    Representa una transacción de gasto, heredada de la clase base Transaction.
    """
    def __init__(self, description, amount):
        if not isinstance(description, str):
            raise ValueError("Description must be a string")
        if not isinstance(amount, (int, float)):
            raise ValueError("Amount must be a number")
        if amount <= 0:
            raise ValueError("Amount must be a positive number for an expense")
        super(Expense, self).__init__(description, -abs(amount), TransactionType.EXPENSE.value)

    def __repr__(self):
        """
        Representación en forma de string de la instancia Expense.
        """
        return f"<Expense(description={self.description!r}, amount={self.amount})>"

class ExpenseSchema(TransactionSchema):
    """
    Esquema para serializar y deserializar objetos Expense usando Marshmallow.
    """
    @post_load
    def make_expense(self, data, **kwargs):
        return Expense(**data)
