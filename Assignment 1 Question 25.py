#Question 25
#Print the Fibonacci series using recursive function
def f(n):
  if n<=0:
    print("Enter the positive number")
  elif n==1:
    return 0
  elif n==2:
    return 1
  else:
    return(f(n-1)+f(n-2))
n=int(input("Enter the number of terms :"))
f(n)
for i in range(1,n+1):
  print(f(i))