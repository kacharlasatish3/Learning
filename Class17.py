# oops
# object-oriented programming structure
# class
# object
# abstraction
# encapsulation
# polymorphism
# Inheritance

# code re usability , scalability

# class => class is an entity, or it's a container
# class contains members(variables) and member functions
class bank:
    # bank_name = "HDFC"

    # constructor => constructing an object
    # __init__ => this a constructor
    def __init__(self, bank_name, account_holder):
        self.bank_name = bank_name
        self.account_holder_name = account_holder

    def create_savings_account(self, name):
        # self.account_holder = name
        print("create savings account ", name)

    def create_current_account(self):
        print(self.bank_name)
        print(self.account_holder_name)
        print("create account")


# object => instance of a class
obj_bank = bank("icici", "chandra")
print(obj_bank.bank_name)
# print(bank.bank_name)
obj_bank.create_savings_account("chandra")
obj_bank.create_current_account()
# obj_bank.account_holder
# self => it represents the current instance of a class

# static variable => which is not depend on object/instance , which can be accessed without instance/object
# Instance variables => variables which are attached to object(self) and accessed with object
# Instance methods => Methods which are accessed with object



