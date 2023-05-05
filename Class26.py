# Pytest => this is built on unit test framework
import string


def addition(x, y):
    return x + y


def subtraction(x, y):
    return x - y


def multiplication(x, y):
    return x * y


# Test with two positive values
# Test with Negative values
# Test with Positive and negative combination
# Test with decimal values
# Test with combination of numeric and decimal values

# The pytest framework automatically identifies the test files and test methods in the given directory

# how to start with pytest
# first we need to install pytest framework
# Create python file with name should start with test_ , example like test_users ,test_login,test_aadhar
# define test method names start with test , test_ :example test_addition_positive_numbers
# how to execute test cases => pytest -v or pytest
# what is the use of -v => it provides in detail information about each test
# how to execute particular test case => pytest -k testcasename , it will search for substring in each test
# for example pytest -k addition , then it will search for all test which name contains addition
# pytest -k test_addition_numeric_decimals, then it will execute only this test
# how to execute particular test file => pytest .\test_addition.py -v
# smoke => We will test high level functionality/positive flow on initial builds
# Regression => We will do in detail testing of functionality to make sure nothing has been broken when new
# enhancement or bug fixes
# Sanity => We will do test on final builds to make sure high level functionality is
# working as well as bug fixes,small enhancements

# In pytest we have concept called mark => we can group test cases by using pytest.mark.groupname
# to execute particular group of test cases pytest -m groupname

# commands
# pytest -v => executes all test cases inside directory
# pytest -k testcasename => to execute particular test case
# pytest testfilename -v  => to execute particular test file name
# pytest -m groupname -v => to execute particular group of test cases
# skip => if we want to skip any test case from execution then we can use @pytest.mark.skip
# xfail => @pytest.mark.xfail , with this even if test case is failed it will not consider as fail
# fixture => fixture is nothing but combination of setup and tear down
# setup => before execution of test method if we want to do some basic functionality
# tear down => this will execute after completion of test method
# where to write this fixtures
# conftest.py => we will add all fixtures here, so it will be accessible to application

import random

l1 = ''.join(random.choices(string.ascii_lowercase +string.ascii_uppercase+
                    string.digits, k=10))
print(l1)
