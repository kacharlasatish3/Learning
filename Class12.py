# Function without parameter
# Function with parameters
# Function with default parameter


# Arguments types
# 1) Positional arguments
# 2) Keyword arguments
# 3)Default arguments
# 4) arbitrary arguments
# 5) keyword arbitrary arguments

# Positional arguments
def create_bank_customer(name, custId, balance, mobile):
    '''
    This function adds bank customer details
    :param name: name of customer
    :param custId:  unique customer id for each customer
    :param balance:  bank balance
    :param mobile: phone number
    :return:
    '''
    customer = {"customername": name, "customerId": custId, "acc_balance": balance, "phone": mobile}
    print(customer)


create_bank_customer(2334, "xyz", 24344, 97666)

# keyword arguments
create_bank_customer(balance=34443, mobile=577888888, custId=3444, name="xyz")


# default arguments => where we will set default value for parameter
def create_bank_customer(name, custId, balance, mobile, ifsccode="HDFC0004566"):
    customer = {"customername": name, "customerId": custId, "acc_balance": balance, "phone": mobile,
                "ifsccode": ifsccode}
    print(customer)


# arbitrary arguments
# here args data type will be tuple
def addition(*args):

    total = 0
    for i in args:
        total += i

    print(total)


addition()
addition(4)
addition(4, 5)
addition(5, 6, 7)
addition(5, 8, 9, 9)

# keyword arbitrary arguments
# **kwargs data type is dictionary
def customer_details(**kwargs):
    for i in kwargs.items():
        print(i)

# x ={"name":"chandra","id":344}
# for i in x.items():
#     print(i)

customer_details(name="xyz", address="ATP", city="anantapur", pincode=454555)

# print first 50 prime numbers by using function
# take start number (20) and end number(60) and print prime numbers between this

# while
# loops
# for,while
l1 =[2,4,67,5777]

i = 0
while i < 10:
     print(i)
     i = i+1



