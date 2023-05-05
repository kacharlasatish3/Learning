# local variables
# global variables

# local variable => this is accessible only inside function

def sample_variables_scope():
    # local variable /local scope , it is accessible only inside function
    x = 10
    x += 2
    print(x)


y = 20
y = 30
# global variable => it can be accessed anywhere
def sample_global_variable_access():
    # to make local variable as global , we need to user global keyword
    global y
    y = 40
    print(y)


sample_global_variable_access()
print(y)

# by using below statement we can access the functions which are defined in another modules
from Class13 import *

customer_detail()