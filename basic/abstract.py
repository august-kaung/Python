# DB connector
from abc import ABC, abstractmethod

# Interface-like abstract class
class DatabaseConnector(ABC):
    @abstractmethod
    def connect(self):
        pass
    
    @abstractmethod
    def disconnect(self):
        pass
    
    @abstractmethod
    def execute_query(self, query):
        pass

class MySQLConnector(DatabaseConnector):
    def connect(self):
        return "Connected to MySQL"
    
    def disconnect(self):
        return "Disconnected from MySQL"
    
    def execute_query(self, query):
        return f"Executing on MySQL: {query}"

class PostgreSQLConnector(DatabaseConnector):
    def connect(self):
        return "Connected to PostgreSQL"
    
    def disconnect(self):
        return "Disconnected from PostgreSQL"
    
    def execute_query(self, query):
        return f"Executing on PostgreSQL: {query}"

# Usage
db_connectors = [MySQLConnector(), PostgreSQLConnector()]
for connector in db_connectors:
    print(connector.connect())
    print(connector.execute_query("SELECT * FROM users"))
    
    
#Payment Gateway
from abc import ABC, abstractmethod

class PaymentGateway(ABC):
    @abstractmethod
    def process_payment(self, amount):
        pass
    
    @abstractmethod
    def refund_payment(self, transaction_id):
        pass
    
    def validate_card(self, card_number):
        # Common validation logic
        return len(str(card_number)) == 16

class StripeGateway(PaymentGateway):
    def process_payment(self, amount):
        return f"Processed ${amount} via Stripe"
    
    def refund_payment(self, transaction_id):
        return f"Refunded transaction {transaction_id} via Stripe"

class PayPalGateway(PaymentGateway):
    def process_payment(self, amount):
        return f"Processed ${amount} via PayPal"
    
    def refund_payment(self, transaction_id):
        return f"Refunded transaction {transaction_id} via PayPal"

# Usage
payment_methods = [StripeGateway(), PayPalGateway()]
for method in payment_methods:
    if method.validate_card("1234567812345678"):
        print(method.process_payment(100))
        
