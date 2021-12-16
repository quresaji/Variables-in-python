def Search(list,ch):
   for x in range(len(list)):
     if ch == list[x]:
         print("The entered Alphabet is available in list",x)
         break
   else:
        print("The entered alphabet is not available in list")

list = ['A','B','C',"D","E","F","G","H","I","J","K","L"]

print(list)
print(len(list))

ch= input("Enter the Alphabet:")
Search(list,ch)
