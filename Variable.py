# I am going to declare variables in python
x=5
y=10
print(x+y)

print(type(x))

y="Sajid"
print(type(y))
"""
A variable name must start with a letter or the underscore character
"""
_s=20
_y=40
print(_s+_y)

# A variable cannot start by number 
my_name="Sajid"

print(type(my_name)) # we are checking the data type of variable
print(type(_s))

# It is difficult to write the variable names in more than one word so there are following ways to do that
# 1. Camel case
#except first letter all letter should be in capital

myVariableName=" Harry"

print(myVariableName)

# 2. Pascal Case

# All first letters will be in capital

MyVariableName="Danny"

print(MyVariableName)

# Snake case
# each word will be separated by and underscore

my_name=" Jack"

print(my_name)
print(type("MyVariableName"))


x = "awesome"

def myfunc():
  x = "fantastic"
  print("Python is " + x)

myfunc()

print("Python is " + x)