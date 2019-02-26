from especial_account import Client
from especial_account import Account, EspecialAccount

paul = Client('Paul Leo', '44 9856453387')
gra = Client('Gra Gadd', '44 7485537387')


account1 = Account([paul], 1, 1000)
account2 = EspecialAccount([gra, paul], 2, 500, 1000)
account1.withdrawal(50)
account2.deposit(300)
account1.withdrawal(190)
account2.deposit(95.15)
account2.withdrawal(937)

account1.statement()
account2.statement()
