# string interpolation/substitution

name= "Sajid Qureshi "

language= "Python"
 # My name is Sajid Qureshi , I am learning python.

msg=" My name is {}, I am learning {}."
print(msg.format(name,language))




#concationation of Name and surname

name="Ajay"
Surname="Parihar"

print(name+" "+Surname)





#String substitution

Teacher=" Anil Dollar "
Language="Python "

msg="I am learning {} from {} sir"
print(msg.format(Language,Teacher))






#F string

print(f'I am learning {Language} from {Teacher} sir 2')

# We are substituting variable inside string


A= 30
B= 4
#The result is 120

print(f" The Product of A and B is {A*B}")









# % Formatting

# in % formattiing we have to use %fomatter %s

#I am learning Python from Anil Dollar sir 

print("I am learning %s from %s sir 3"%(Language,Teacher))

