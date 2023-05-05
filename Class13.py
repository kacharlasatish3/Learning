# Arguments/parameter types
# 1) Positional arguments
# 2) Keyword arguments
# 3)Default arguments
# 4) arbitrary arguments
# 5) keyword arbitrary arguments

def customer_detail(name, sal, ifsccode="ICICI", *args, **kwargs):
    print(name)
    print(sal)
    print(ifsccode)
    print(args)
    print(kwargs)


customer_detail("chandra", 1212, "SBI4545", 2, 3, 4, address="ATP", state="AP")

# when we have combination of all arguments => keep in order as
# Positional arguments,default arguments , arbitrary arguments,keyword arbitrary arguments

# pass ,break , continue ,return

# def ss():

# pass => when we want to define a function or block (if,for,while) with out defining any logic/piece of
# code inside that then we will use pass keyword to continue execution without throwing any error
# after pass if I define any code it will execute as it is
x = 8
if x > 7:
    pass

for i in range(10):
    pass


def sample():
    pass


sample()

names = ["chandra", "satish", "lohitha", "lakhmi", "gagan", "naresh", "rs"]

# break => this is used to break the iteration
for i in names:
    if i == "gagan":
        print(i)
        break

    print("still not found")

print("//////continue/////")
# continue => skip the particular iteration and continue further execution
for i in range(5):
    if i == 3:
        continue
    print(i)

# pass,break,continue
# return

# variables, operators ,data types,if,for,while , break,continue
