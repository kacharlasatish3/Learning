# List => Create ,Read,update,delete  => list is supporting all operations
# list mutable/changeable data type => the element inside list can be changeable and deleted
# tuple => immutable/unchangeable data type => the element inside tuple can not be changed or deleted
# tuple => works like constant
# list =>[]
# Tuple => ()
tuple1 = (1, 2, 'python', 455.45)
print(type(tuple1))
t1 = 1,
print(type(t1))
# CRUD
# Create
tuple1 = (1, 2)
# Read
# indexing ,slicing
print(tuple1[0])
print(tuple1[0:2])
# update  => will not support by tuple
# tuple1[0] = 7
# delete => individual item deletion will not support by tuple
# del tuple1[0]
del tuple1  # => complete object can be deleted
# print(tuple1)

# dictionary
bank_details = ["chandra", 345445, 455555, 'Sai Nagar']
# dictionary => key and value pair
bank_customer = {"name": "chandra", "cusid": 345445, "balance": 34555, "address": "Sai Nagar"}
print(bank_customer)
print(type(bank_customer))
# keys can not be duplicate in dictionary
# CRUD
# Create
bank_customer = {"name": "chandra", "cusid": 345445, "balance": 34555, "address": "Sai Nagar",
                 "accounts": ["savings account", "current account"]}
# Read => we will read data based on key
print(bank_customer["name"])
print(bank_customer.get("name"))
# difference between accessing value based on get method and accessing with [key] ,
# the get method will handle ,if key is not exists in dictionary it will throw none
# whereas [key] will give key error
# print(bank_customer["name1"]) => this will give error
print(bank_customer.get("name1"))  # => this will handle error and return None

# update
bank_customer["name"] = "Chandra R"
bank_customer["first_name"] ="Rayavaram"
print(bank_customer)

# delete
del bank_customer["name"]
print(bank_customer)

# del bank_customer => this will delete complete object

# the key should be immutable data type
# the key can be string ,tuple,int
# but it can not be list => mutable data type

customer ={"name":"Python",1:1000,33.33:46655,(23,33):"Tuple key"}
print(customer)