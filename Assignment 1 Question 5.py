#Question 6
#Print the reverse of the number
n=int(input("Enter the number : "))
l=len(str(n))
s=0
for i in range(0,l):
  m=n%10
  s=(s*10)+m
  n//=10
print(s)


