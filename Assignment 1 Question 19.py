#Question 20
#Get a sequence of numbers from the user and store the numbers in a list. Add them and print the result
n=(int(input("Enter the number of elements :")))
l=[]
s=0
for i in range(0,n):
  p=int(input("Enter the "+str(i+1)+"th element :"))
  l.append(p)
print("List =",l)
for i in l:
  s+=i
print("The sum of elements in list is",s)
