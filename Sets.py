#Sets is undordered , meaning: the items will appear in random order
# Refresh this page to see the change in result

# So now I am going to create a set , set will be created in {}
#Duplicates are not allowed in set
School={'Name','Class','Gender'}

print(School)

print(type(School))

School1={'Name':'Sajid'}

print(School1)

print(type(School1))


School={" Date", 'Gender ', " Caste"}
print(School)

print(len(School))

print(len(School1))

School2=("Ajay", "Kartik", "Abhishek")
print(len(School2))

School3=['Jay',"Veeru"]


print(School3[1])



print(f'The Length of School list2 is {len(School2)}')

School={"Ajay"}

print(School)

School4={" Far","Ran"," run"}

print(School4)

School4.discard("run")

print(School4)



#pop


School5={"Face", " Rough", "Tab"}


x=School5.pop()
print(School5)

print(x)


#Clear

School5.clear()

print(School5)

#Delete

del School5

   
print(School5)

friends={'Ravi',"Akash","Rohit"}
"""
for var in set/list/dict/tuple:

"""
for x in friends:

    print('Hellp {x}, How are you ')



    #To combine two sets of a python program we need Union

    Team1={'Harry','Ron','Hermoinie'}
    Team2={'Draco','Crab',"Goy"}


    Team=Team1.union(Team2)

    print(Team)