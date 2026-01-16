class Bank:
    def __init__(self,Acc_No,Balance):
        self.Acc_No=Acc_No
        self.Balance=Balance
    def Deposit(self,amount):
        if(amount<=0):
            print("Deposit amount must be a positive number")
        else:
            self.Balance+=amount
            print(f"Amount Deposited Successfully Current Balance is ::{self.Balance}")
    def Withdrawal(self,amount):
        if (amount <= 0):
            print("Deposit amount must be a positive number")
        elif(self.Balance<amount):
            print("Your Bank Account Doesn't have Sufficient Balance")
        else:
            self.Balance-=amount
            print(f"Withdrawal Successful and current Balance is ::{self.Balance}")
    def __del__(self):
        print("object deleted successfully")

obj1=Bank(1001,25000)
obj1.Deposit(5000)
obj1.Withdrawal(10000)
