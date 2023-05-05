# return

# we will use return in the functions

def addition(x, y):
    return x + y


temp = addition(3, 4)
print(temp)
# difference between break and return => return will get some data back where as break will just stop the iteration
# Create customer
# Read customer
# update customer
# delete customer

customers = []


def create_customer(name, custid, balance, ifsccode):
    cus_temp = {"name": name, "CustId": custid, "Balance": balance, "IFSCCode": ifsccode}
    customers.append(cus_temp)


def read_customer(custId):
    for item in customers:
        if item["CustId"] == custId:
            return item


def update_customer(custId, update_name):
    for item in customers:
        if item["CustId"] == custId:
            item["name"] = update_name
            return "updated successfully"


def delete_customer(custId):
    for i in range(len(customers)):
        temp = customers[i]
        if temp["CustId"] == custId:
            del customers[i]
            break


create_customer("john", 243333, 2000, "HDFC0012")
create_customer("Kelvin", 34566, 2000, "HDFC0012")
create_customer("Stephen", 78778, 2000, "HDFC0012")

temp = read_customer(34566)
print(temp)

update_customer(78778, "chandra")

delete_customer(243333)

print(customers)
