
import datetime

class Bank:

    def __init__(self, total=0.00) -> None:
        self.total=total

    def Deposit(self,amount):
        if amount>0:
            self.total+=amount
           
        
    def Withdraw(self,amount):
        if self.total>=amount:
            self.total-=amount

    def CurrentAmount(self):
        return self.total


bank= Bank(0)
system = True
transactionlist=[]
choice=False
while system:
    opt= input("Choose: deposit, withdraw, balance, quit ::")
    if opt=="deposit":
        choice=True
        while choice:
            try:
                damt=input("Deposit Amount:")
                bank.Deposit(float(damt))
                print(bank.CurrentAmount())
                transactionlist.append({"Type":"Deposit","Amount":damt,"Balance":bank.CurrentAmount(),"Date":datetime.datetime.now()})
                
                choice=False
            except:
                print("Must be a valid number")
    elif opt=="withdraw":
        choice=True
        while choice:
            try:
                amount= float(input("Withdraw Amount:"))
                bank.Withdraw(amount)
                print(bank.CurrentAmount())
                transactionlist.append({"Type":"Withdraw","Amount":amount,"Balance":bank.CurrentAmount(),"Date":datetime.datetime.now()})
                choice=False
            except Exception as e:
                print(e)    
    elif opt=="balance":
        print(bank.CurrentAmount())
    elif opt=="quit":
        print(bank.CurrentAmount())
        system=False
    else:
        print("Please select from the following options")
print(transactionlist)
with open("transaction",'w') as file:
    for transaction in transactionlist:
        file.write("%s\n" % f"Type:{transaction['Type']}, Amount:${transaction['Amount']}, Balance:${transaction['Balance']},Date:{transaction['Date']}" )

    
    

