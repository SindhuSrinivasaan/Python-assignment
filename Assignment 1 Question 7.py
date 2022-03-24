#Question 7
#Print the Fibonacci series
n=int(input("Enter the no of terms : "))
n1,n2=0,1
if n<=0:
  print("Enter the positive number")
elif n==1:
  print(n1)
else:
  print(n1,n2,end=" ")
  for i in range(3,n+1):
    nth=n1+n2
    print(nth,end=" ")
    n1=n2
    n2=nth