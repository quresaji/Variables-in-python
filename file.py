filename=input("Please Enter the filename: ")
filename=filename+'.txt'

# Always open the file 

fo=open(filename,'a') 

content=input('Please enter my content')
fo.write(content)

#Always close the file

fo.close()

fo=open(filename,'rt') # where  read t text mode

mycontent=fo.read()
print(f"The length is {len(mycontent.split())}")

#split is a string function, it accepts two parameters both are optionals, separator, maxsplit

fo.close()