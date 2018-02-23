class Account:
    # create a constructor
    # below we initialize the object
    def __init__(self,acno,amount,name,type):
        self.acno = acno
        self.amount = amount
        self.name = name
        self.type = type

    #  parse a parameter to allow hold deposited cash
    def deposit(self,depamount):
        if depamount < 50:
            print("Below Deposit Threshold")
        else:
            self.amount=self.amount  + depamount
            print("Deposit of ", depamount,"Successful")


    def withdraw(self,withdrawn):
        if withdrawn > self.amount:
            print("Insufficient Funds")
        else:
            self.amount = self.amount - withdrawn
            print("Withdrawal of ", withdrawn, "Successful")


    def checkDetails(self):
        print("---Account Deatails--")
        print(self.acno)
        print(self.type)
        print(self.name)
        print(self.amount)

    def changetype(self,newtype):
          self.type = newtype


    def checkbal(self):
        print("Current Bal: ", self.amount)


#  create the account object
ob  = Account(100003,50000,"Joe","Personal")
ob.withdraw()
# ob.checkbal()
ob.checkDetails()














