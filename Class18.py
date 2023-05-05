# Class methods
# Static methods => methods/variables which can be accessed without object

class bank:
    bank_name = "HDFC"

    def get_customer_detail(self):
        print(self.bank_name)
        self.get_bank_atms()
        self.get_bank_details("sbi","atp")
        self.get_bank_loans()
        return "savings account customer"

    def get_bank_atms(self):
        print("bank digital atms")

    @staticmethod
    def get_bank_details(name, address):
        print(name, " bank details ", address)

    @classmethod
    def get_bank_loans(cls):
        print("Personal loans")

    @classmethod
    def get_bank_employees(cls):
        # accessing class variables/global vaiables
        print(cls.bank_name)

        #  we can not access instance method
        # print(cls.get_customer_detail())

        # accessing static methods
        cls.get_bank_details("icici", "ATP")

        # accessing class methods
        cls.get_bank_loans()
        print("1000 employees in bank")

print("/////Instance methods///")
# Instance methods => methods which can be accessed with object
# Inside instance methods => we can access instance methods /instance variables by using self
#  we can access static methods , class methods
obj = bank()
obj.get_customer_detail()

# static methods => methods which can be accessed without object
# Inside static methods => we can only access static variables and static methods
bank.get_bank_details("icici", " ATP ")

# class method
print("//////class methods///")
bank.get_bank_employees()
# class methods => class methods can be accessed without object
# Inside class method => we can access another class methods,class/static variables,static methods
