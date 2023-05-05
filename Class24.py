# Automation with python
# Application => any application mainly contains 3 layers
# UI (user interface) => Automation for UI  => Selenium(UI Framework) with Python/Robot framework,playwright
# middle layer/service/api => data validation in Rest api
# database => Manually
# Pytest Framework


# API Automation
# API (application program interface)
# this will transfer data between UI and database
# Postman,soapui,swagger
# Postman => manual api testing tool
# CRUD
# Create => Post
# Read => Get
# update => Put /Patch
# Delete => Delete
# API Methods
# Get  => To read existing data
# Post => To create new data
# Put   => To update data
# Patch => To update single column
# Delete => To delete record

# To test API what are the required things basic
# API method => We should know what API method we are going to test
# URL/endpoint => api location
# Headers
# Body


# Get => to read data , we can read complete, or we can read specific data
# Headers =>  example =>Content-Type :application/json
#  url/endpoint =>https://gorest.co.in/public/v2/users
# Verify Response => Status code => it should be 200
                  # => Data validation

# Get particular data
# sample => https://gorest.co.in/public/v2/users/1087446
# Path parameter => we will append the value with api by using /
# Query parameter => by using ?= we will pass multiple fields/columns values
                # => https://reqres.in/api/users?page=2&id=7
