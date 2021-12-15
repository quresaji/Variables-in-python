
filename = input("Please enter the filename")
filename=filename+'.txt'

try: # try is used to test the block of code for errors
     fo=open(filename,'r')

     fo.close()

except: #except is used to handle the error
    print("Unable to open the file ")


filename=input("Please enter the filename")
filename=filename+".txt"
try:
  f = open(filename.txt,'w')
  try:
    f.write("XYZ")
  except:
    print("Something went wrong when writing to the file")
  finally:
    f.close()
except:
  print("Something went wrong when opening the file")
