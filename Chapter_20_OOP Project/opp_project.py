from bank_accounts import *

RamGopal = BankAccount(1000, "Ram Gopal")
Suraj = BankAccount(20000, "Suraj")

RamGopal.getBalance()
Suraj.getBalance()

RamGopal.deposit(500)
RamGopal.withdraw(250)
RamGopal.transfer(1000, Suraj)
RamGopal.transfer(200, Suraj)

Rahul = InterestRewardsAcct(1000, "Rahul")
Rahul.getBalance()
Rahul.deposit(100)
Rahul.transfer(100, Suraj)

Sager = SavingAcct(1000, "Sager")
Sager.getBalance()
Sager.deposit(100)
Sager.transfer(1000, Suraj)