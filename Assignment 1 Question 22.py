#Question 22
'''Get a sequence of numbers from the user and store them in a list. Update the values in the
list by adding a constant value obtained from the user to all the elements in the list and store the updated values in a new list'''
n=(int(input("Enter the number of elements :")))
l,b=[],[]
s=0
for i in range(0,n):
  p=int(input("Enter the "+str(i+1)+"th element :"))
  l.append(p)
print("List =",l)
a=int(input("Enter the constant added to each of the number :"))
for i in l:
  k=i+a
  b.append(k)
print(b)