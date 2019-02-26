class Client:
    def __init__(self, name, phone,):
        self.name = name
        self.phone = phone

class Account:
    """
    Account whith statement.
    """


    def __init__(self, client, number, balance = 0):
        self.client = client
        self.number = number
        self.balance = 0
        self.operations = []
        self.deposit(balance)

    def summary(self):
        print('Account number: %s Balance: %10.2f' %(self.number, self.balance))

    def withdrawal(self, value):
        if self.balance >= value:
            self.balance -= value
            self.operations.append(['Withdrawal', value])

    def deposit(self, value):
        self.balance += value
        self.operations.append(['Deposit', value])

    def statement(self):
        print('Account Statement Number %s: ' %self.number)
        for op in self.operations:
            print('%10s %10.2f' %(op[0],op[1]))
        print('%10s %10.2f\n' %('Balance: ', self.balance))
