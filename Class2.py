address = '23/44 ,3rd cross,BLR'
pincode = 5646466
# complete_address = address + pincode

#  we need data type conversion
complete_address = address + " " + str(pincode)
print(complete_address)

# Implicit
# explicit

# Implicit # it will automatically convert from one data type to another data type ,
# if both data types are from same family , it will convert to higher data type
balance = 5677  # int
intrest = 456.34  # float
total = balance + intrest  # float
# 5677.00 + 456.34 # 6133.34
#
print(total ," : ",type(total))

# explict => we will convert to specific data type explicitly
total = balance + int(intrest)
print(total, " : ", type(total))

# string to int
count = '45'
remaining = 56
total_count = int(count)+ remaining
print(total_count) # 101

isvalid = 'True'
print(bool(isvalid))
a = 0
print(bool(a))
b = 1
print(bool(b))
c = 2
print(bool(c))
x ='0'
print(x ," ",bool(x))

print("///////")
# string will have inbuilt functionalities
name  ='python'
print(name.upper())


