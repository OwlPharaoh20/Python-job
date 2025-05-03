#A module is basically a file containing a set of functions you want to include in your application.

#core modules 
import datetime
from datetime import date
from time import time as current_time


#pip module 
from camelcase import CamelCase



#Import custom module
import validator
from validator import validate_email



#today = datetime.date.today()
today = date.today()
timestamp = current_time()


c = CamelCase()
print(c.hump('hello world'))

email = "test#test.com"
if validate_email(email):
    print('Email is valid')
else:
    print('Email is invalid')



print(timestamp)