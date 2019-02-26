class Client:
    def __init__(self, name, phone):
        self.name = name
        self.phone = phone

class Account:
    """
    Account whitout statement.
    """


    def __init__(self, client, number, balance = 0):
        self.client = client
        self.number = number
        self.balance = balance

    def summary(self):
        print('Account number: %s Balance: %10.2f' %(self.number, self.balance))

    def withdrawal(self, value):
        if self.balance >= value:
            self.balance -= value

    def deposit(self, value):
        self.balance += value
