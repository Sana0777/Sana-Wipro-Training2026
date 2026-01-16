from abc import ABC,abstractmethod

class Bank(ABC):
    @abstractmethod
    def Loan(self):
        pass
    @abstractmethod
    def Interest(self):
        pass
class Tax(ABC):
    @abstractmethod
    def TaxPay(self):
        pass
class SBI(Bank):
    def Loan(self):
        print("Loan is available")
    def Interest(self):
        print("Interest rate is 6%")
    def TaxPay(self):
        print("Tax is paid")
obj1=SBI()
obj1.Interest()
obj1.Loan()
obj1.TaxPay()
