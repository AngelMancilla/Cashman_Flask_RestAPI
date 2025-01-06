from flask import Flask, request, jsonify
from marshmallow import ValidationError
from cashman.model.expense import Expense, ExpenseSchema
from cashman.model.income import Income, IncomeSchema
from cashman.model.transaction_type import TransactionType

app = Flask(__name__) # Create the Flask app instance

# Predefined list of transactions to serve as a simple in-memory database
transactions = [
    {"type": "income", "description": "Salary", "amount": 5000},
    {"type": "income", "description": "Dividends", "amount": 200},
    {"type": "expense", "description": "pizza", "amount": 50},
    {"type": "expense", "description": "Rock Concert", "amount": 100}
]

def get_transactions_by_type(transaction_type):
    """
    Helper function to filter transactions by type.
    
    Args:
        transaction_type (TransactionType): Type of transaction to filter (Income or Expense)
        
    Returns:
        list: List of transactions of the specified type
    """
    return filter(lambda t: t['type'] == transaction_type.value, transactions)

@app.route('/incomes', methods=['GET', 'POST'])
def incomes():
    """
    Endpoint to handle income transactions.
    
    - GET: Retrieve all income transactions.
    - POST: Add a new income transaction.
    
    Returns:
        - JSON response with income transactions on GET.
        - HTTP 204 status on successful POST.
        - HTTP 400 with validation errors on invalid POST data.
    """
    if request.method == 'POST':
        try:
            income = IncomeSchema().load(request.get_json())
            transactions.append(income)
            return '', 204
        except ValidationError as err:
            return jsonify(err.messages), 400

    schema = IncomeSchema(many=True)
    incomes = schema.dump(get_transactions_by_type(TransactionType.INCOME))
    return jsonify(incomes)

@app.route('/expenses', methods=['GET', 'POST'])
def expenses():
    """
    Endpoint to handle expense transactions.
    
    - GET: Retrieve all expense transactions.
    - POST: Add a new expense transaction.
    
    Returns:
        - JSON response with expense transactions on GET.
        - HTTP 204 status on successful POST.
        - HTTP 400 with validation errors on invalid POST data.
    """
    if request.method == 'POST':
        try:
            expense = ExpenseSchema().load(request.get_json())
            transactions.append(expense)
            return '', 204
        except ValidationError as err:
            return jsonify(err.messages), 400

    schema = ExpenseSchema(many=True)
    expenses = schema.dump(get_transactions_by_type(TransactionType.EXPENSE))
    return jsonify(expenses)

if __name__ == "__main__":
    """
    Entry point of the application. 
    Starts the Flask development server to handle incoming requests.
    """
    app.run()
