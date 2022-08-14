class Account:

  def __init__(self, filepath):
    self.filepath=filepath
    with open(filepath, "r") as file:
      self.balance=float(file.read())

  def withdraw(self, amount=0):
    self.balance-=amount
    self.save()
  
  def deposit(self, amount=0):
    self.balance+=amount
    self.save()
  
  def save(self):
    with open(self.filepath, "w") as file:
      file.write(str(self.balance)) 

class Checking(Account):
  """ Checking class to transfer money from Account """
  type="check class"

  def __init__(self, filepath, fee):
    Account.__init__(self, filepath)
    self.fee=fee

  def transfer(self, amount=0):
    self.balance-=amount * self.fee
    self.save()

""" 
account=Account("./balance.txt")
print(account.balance)

account.withdraw(10)
print(account.balance) 
"""

checking=Checking("./balance.txt", 0.15)
print(checking.balance)

checking.transfer(50)
print(checking.balance)
print(Checking.type)
print(checking.type)