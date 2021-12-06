"""
Functions are reusable block of code
Function only runs when it is called
You can pass Data/Parameter/Argument, known as parameters into a function

A function can return data as a result

Function defination is a one time process
"""

def getMyName(name='Ajay'):# name is formal argument
    print(f"Hello {name}, How are you ")
    print("Hello "+name+",How are you ")#Varibale substitution

getMyName('Sajid')# Actual Argument


#Default Argument

getMyName()

#Arbitrary Argument
def getMystudent(*std):
    print("Hello"+ std[2])
getMystudent('Sajid',"Ajay","Dipesh")

def productMyNumber(x,y):
    return x*y

Result= productMyNumber(90,68)
print(f" The result is {Result}")

# pass statement (pass is a keyword , it  is a null statement that means nothing

def sayHello():

    pass

sayHello()



