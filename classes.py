#A class is like a blueprint for creating objects. An object has properties and methods.(Functions) associated with it. Almost everything in python is an object.

#create class
class User:
    # constructor
    def __init__(self, name, email, age):
        self.name = name
        self.email = email
        self.age = age

    def greeting(self):
        return f'My name is {self.name} and I am {self.age}'

    def has_birthday(self):
        self.age += 1


#Extend class 
class Customer(User):
   # constructor
  def __init__(self, name, email, age):
        self.name = name
        self.email = email
        self.age = age
        self.balance = 0 


  def set_balance(self, balance):
    self.balance = balance


  def greeting(self):
    return f'My name is {self.name} and I am {self.age} and my balance is {self.balance}'



# Init User object
brad = User('Brad Traversy', 'Zk6k3@example.com', 37)

#Init customer object 
janet = Customer('Janet Johnson', 'jZk6k3@example.com', 27)

janet.set_balance(500)
print(janet.greeting())

brad.has_birthday()
print(brad.greeting())