from banknani import Client
from banknani import Account

paul = Client('Paul Leo', '44 9856453387')
gra = Client('Gra Gadd', '44 7485537387')

print('Name: %s  Phone:  %s' %(paul.name, paul.phone))
print('Name: %s  Phone:  %s' %(gra.name, gra.phone))

account1 = Account([paul], 1, 7000 )
account2 = Account([gra], 2, 1500)
account1.summary()
account2.summary()

