# Function inside function => inner function
# iterator
# generator
# decorator

# iterator => iteration
l1 = [23, 45, 56, 77, 58]
# for i in l1:
#     print(i)
itr = iter(l1)
temp = next(itr)
print(temp)
print(next(itr))
print(next(itr))
print(next(itr))
print(next(itr))
print(next(itr, "stop iteration"))

# generator => it uses a concept of yield key word and returns data and executes next statements
# return , yield
print("//////generator///////")


# yield => it sends/returns the data and executes next statement

# difference between return vs yield => return will stop the execution and sends the object whereas yield
# will return data and executes next statement

def sample_yield():
    yield 1
    yield 2
    yield 3


for i in sample_yield():
    print(i)


def sample_function():
    users = [{"id": 7, "email": "michael.lawson@reqres.in", "first_name": "Michael", "last_name": "Lawson",
              "avatar": "https://reqres.in/img/faces/7-image.jpg"},
             {"id": 8, "email": "lindsay.ferguson@reqres.in", "first_name": "Lindsay", "last_name": "Ferguson",
              "avatar": "https://reqres.in/img/faces/8-image.jpg"},
             {"id": 9, "email": "tobias.funke@reqres.in", "first_name": "Tobias", "last_name": "Funke",
              "avatar": "https://reqres.in/img/faces/9-image.jpg"},
             {"id": 10, "email": "byron.fields@reqres.in", "first_name": "Byron", "last_name": "Fields",
              "avatar": "https://reqres.in/img/faces/10-image.jpg"},
             {"id": 11, "email": "george.edwards@reqres.in", "first_name": "George", "last_name": "Edwards",
              "avatar": "https://reqres.in/img/faces/11-image.jpg"},
             {"id": 12, "email": "rachel.howell@reqres.in", "first_name": "Rachel", "last_name": "Howell",
              "avatar": "https://reqres.in/img/faces/12-image.jpg"}]
    for i in users:
        yield i


for i in sample_function():
    print(i)

# decorator
# function
# inner function
print("//////decorator/////")


# def customer_address():
#     return "ATP"

def get_bank_details():
    def customer_address(location):
        return "ATP", location

    # print(customer_address())
    # print("HDFC bank")
    return customer_address


temp = get_bank_details()
print(temp)
print(temp("AP"))


# decorator => extending the functionality of a function without modifying it , by passing function as parameter

def division_decorator(func1):
    print("Entered into decorator")

    def inner_condition_check(a, b):
        if b > 0:
            result = func1(a, b)
            print("result from decorator ", result)
        else:
            print("b is not greater than 0 , so to avoid exception we are not executing")

    return inner_condition_check


@division_decorator
def divison(x, y):
    print("entered into divison")
    return x / y


divison(5, 4)
divison(5, 0)
