# I am creqating a python dictionary 

Marx={
#P:V ( where P stands for property and V stands for value)
"Brand":"Tata",

"Model":"Nexon",

"Year":"2021"

}

print(Marx)

#dictName [PropertyName]

print(" I have a "+ Marx["Brand"]+'  '+Marx["Model"]+"Car")

print(f" I have a {Marx['Brand']}  {Marx['Model']} Car ")



Friend={

'Name':'Ajay ',

"Age":"22"
}

#Now I want to change the age

Friend['Age']="23"

print(Friend)

# I am going to add a new property

#Friend['New property name ']='Value'

Friend['Address']= 'Neemuch'
print(Friend)

#now I am going to remove a property called Age

del Friend['Age']

print(Friend)

print(Friend["Address"])

#Access the friend name

print("My Frined Name is "+Friend.get("Name"))