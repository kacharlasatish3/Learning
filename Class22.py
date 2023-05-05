# Exception handling
# str1 = None
# name = None
# 2/0
# print(name.upper())
# x = 10
# y = 10
# print(x + y)
# z ="2"
# 1+z
#
# try ,except ,finally

# try => the logic/code which may throw error will keep inside try block
# except => when ever exception occurred this block will execute
# finally => whether exception occurred or not this will execute
# else => if error not occurred in try block then this else block will execute

import logging
logging.basicConfig(filename="logfile.log",format='%(asctime)s - %(message)s',level=logging.DEBUG)
try:
    x = 1
    y ="2"
    x+y
    # print("completed calculation")
    # x/0

except AttributeError as ex:
    logging.info(ex)
    print(ex)
except ZeroDivisionError as ex:
    print("received zero error ",ex)
    logging.info(ex)
except Exception as ex:
    print("Exception occured in calculation ",ex)
    logging.info(ex)
else:
    print("try else block executed")
finally:
    print("finally block executed")

print("I am  out side from try and except block")