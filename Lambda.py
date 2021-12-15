# Lambda function is a anonymous function
# It can take any number of arguments but can only have one expression


#Lambda arguments : expression

#Lambda Input:output

x=lambda a: a*15

print(x(90))


print(x)



def myfunc(n):
  return lambda a: a*n

  mydoubler= myfunc(78)

  print(mydoubler(11))


