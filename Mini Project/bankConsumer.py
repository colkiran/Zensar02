from BankPackage import BankInfo as BNK


acct1 = BNK.Account(5000, "Sachin")
acct1.Deposit(1000)
acct1.Withdrawal(2000)
print(acct1)

print("-" * 40)

acct2 = BNK.Account(5000, "Ali")
acct2.Deposit(500)
acct2.Withdrawal(250)
print(acct2)

print("-" * 40)

if(acct1 == acct2):
    print("Thay have equal balance")
else:
    print("Thay have different balance")

print("-" * 40)

if(acct1 != acct2):
    print("Oops!!! they are not equal")
else:
    print("wow!!!  they are equal")
