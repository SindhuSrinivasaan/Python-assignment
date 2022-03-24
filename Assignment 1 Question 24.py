#Question 24
#Find the factorial of a number using recursive function
def f(n):
  if n==1:
    return 1
  else:
    return n*f(n-1)
n=int(input("Enter the number of terms :"))
f(n)