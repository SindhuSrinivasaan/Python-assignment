#Question 21
'''Get a sequence of numbers from the user and store them in a list. Update the values in the
list by adding a constant value obtained from the user to all the elements in the list'''
n=(int(input("Enter the number of elements :")))
l=[]
s=0
a=int(input("Enter the constant added to each of the number :"))
for i in range(0,n):
  p=int(input("Enter the "+str(i+1)+"th element :"))
  l.append(p+a)
print("List =",l)