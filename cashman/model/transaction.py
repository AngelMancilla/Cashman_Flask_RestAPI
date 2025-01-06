import datetime as dt
from marshmallow import Schema, fields, validate
from .transaction_type import TransactionType

class Transaction(object):
    """
    Representa una transacción financiera genérica.
    """
    def __init__(self, description, amount, type):
        if not isinstance(description, str):
            raise ValueError("Description must be a string")
        if not description.strip():
            raise ValueError("Description must not be empty")
        if not isinstance(amount, (int, float)):
            raise ValueError("Amount must be a number")
        if amount == 0:
            raise ValueError("Amount must not be zero")
        if not isinstance(type, str):
            raise ValueError("Type must be a string")
        
        self.description = description
        self.amount = amount
        self.created_at = dt.datetime.now()
        self.type = type

    def __repr__(self):
        """
        Representación en forma de string de la instancia Transaction.
        """
        return f"<Transaction(description={self.description!r}, type={self.type})>"

class TransactionSchema(Schema):
    """
    Esquema para serializar y deserializar objetos Transaction usando Marshmallow.
    """
    description = fields.Str(required=True, validate=validate.Length(min=1))
    amount = fields.Number(required=True)
    created_at = fields.DateTime(dump_only=True)
    type = fields.Str(
        required=True,
        validate=validate.OneOf([member.value for member in TransactionType])
    )
