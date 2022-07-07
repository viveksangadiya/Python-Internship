from operator import concat
from unicodedata import name


def my_function():
    name="vivek sangadiya"
    contact=9898801316
    return name,contact
name,contact=my_function()
print("Name :",name)
print("Contact :",contact)