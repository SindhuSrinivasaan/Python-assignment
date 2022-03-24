#Question 14
#Print the sum of ‘n’ numbers from the user 
n=int(input())
s=0
if n<0:
  print("Enter the positive number")
else:
  for i in range(1,n+1):
    s+=i
  print(s)

