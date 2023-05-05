# Class
# object
# abstraction
# polymorphism
# Inheritance

#  The below are concepts inside class
# Constructor
# Self
# Instance methods
# Class methods
# Static methods

# abstraction => abstraction is nothing but providing the functionality to user by hiding internal
# details/implementation
# encapsulation => Encapsulation is used to restrict access to methods and variables

# private => we will make it as private by using __
class bank:

    def __init__(self, atmcard, pin):
        self.__atm_card = atmcard
        self.__pin = pin

    def __with_draw(self, amount):
        balance = 5000
        if self.__atm_card == 354657676 and self.__pin == 3466:
            if amount < 10000 and amount <= balance:
                return str(amount) + " withdrawn "
        else:
            return "you don't have sufficient balance"

    def with_draw_money(self, amount):
        return self.__with_draw(amount)

    # def addition(self, x, y):
    #     return x + y
    #
    # def addition(self, x, y, z):
    #     return x + y + z
    #
    # def addition(self, x, y, d, a):
    #     return x + y + d + a
    def addition(self,*args):
        total=0
        for i in args:
            total+=i
        return total

    def customer_details(self,**kwargs):
        for i in kwargs.items():
            print(i)


obj_bank = bank(354657676, 3466)
obj_bank.with_draw_money(4000)
print(obj_bank.addition(3,4,5,6))
print(obj_bank.addition(3,4))
obj_bank.customer_details(name="xyz", address="ATP", city="anantapur", pincode=454555)

# polymorphism => it contains two things => Over loading , Overriding
# Over loading => In same class defining methods with same name with different signature =>
# but python by default will not support overloading

#  how to achieve overloading in python => by using *args ,**kwargs

# poly => many , morphism => forms => manyforms
#  defining same function name with different signature
# MRO => method resolution order
