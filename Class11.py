# functions
# functions is nothing but piece of code or logic which is related each other
# re usability of code , instead of changing in multiple places , if we change in one place it automatically updates every where

# function without parameter
def sample():
    print("my first function")


sample()
sample()


def get_my_address():
    print("Satish,#344,Bangalore,KA,543434")
    print("i am working as IT employee")


get_my_address()

print("/////function with parameter//////")

# function with parameter
employees = []

# this function is used to add new employees
def my_employee_names(name, department):
    emp = {"Name": name, "Department": department}
    employees.append(emp)


my_employee_names("chandra", "HR")
my_employee_names("lakshmi", "IT")
my_employee_names("naresh", "ADMIN")
my_employee_names('satish', "FINANCE")
print(employees)


def addition(a,b):
    print(a+b)

addition(3,4)
addition(5,6)
addition(7,8)

l1 =[]
l1.extend("CA,BD#12,2ndFloor")
print(l1)
l1.extend(["HC","EC"])
print(l1)
for i in ["HC","EC"]:
    print(i)

print("///function with default parameter////")

# function with default parameter
vaccine_details =[]
def create_vaccine_details(name,vaccine_name,city="ATP"):
    details = {"Name":name,"vaccinename":vaccine_name,"City":city}
    vaccine_details.append(details)


create_vaccine_details("chandra","Covishield")
create_vaccine_details("satish","Covishield")
create_vaccine_details("naresh","Covishield")
create_vaccine_details("rishith","Covishield","BLR")
print(vaccine_details)