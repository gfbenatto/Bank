from banknani2 import Client
from banknani2 import Account

paul = Client('Paul Leo', '44 9856453387')
gra = Client('Gra Gadd', '44 7485537387')

print('Name: %s  Phone:  %s' % (paul.name, paul.phone))
print('Name: %s  Phone:  %s' % (gra.name, gra.phone))

account1 = Account([paul], 1, 7000)
account2 = Account([gra], 2, 1500)

account1.withdrawal(37)
account2.withdrawal(91)
account1.deposit(177)
account2.deposit(10.17)
account2.withdrawal(1980)
account1.summary()
account2.summary()
account1.statement()
account2.statement()
