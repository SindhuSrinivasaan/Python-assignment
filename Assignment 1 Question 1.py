#Question 2
#Print the sum of odd and even numbers in a given range 
n=int(input("Enter the initial range of number : "))
m=int(input("Enter the final range of number : "))
s,k=0,0
for i in range(n,m):
  if i%2==0:
    s+=i
  else:
      k+=i
print("Sum of even numbers = ",s)
print("Sum of odd numbers = ",k)