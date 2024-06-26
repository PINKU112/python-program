# create account class with 2 attributes - balance and account no. & create method for debit, creadit and printing the total balance.

class account:
    def __init__(self,balance, acno):
        self.balance = balance
        self.acno = acno

    def debit(self,amount):
        self.balance -= amount
        print("rs.",amount,"was debited")
        print("total balance= ",self.get_balance())
    def credit(self,amount):
        self.balance += amount
        print("rs.",amount,"was credited")
        print("total balance = ",self.get_balance())
    def get_balance(self):
        return self.balance

acc1 = account(10000,12345)
acc1.debit(1000)
acc1.credit(500)
acc1.credit(45000)              
              




