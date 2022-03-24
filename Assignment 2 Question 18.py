#Question 19
'''Write a program to compute:
a. f(n)=f(n-1)+100 when n>0
b. and f(0)=1
c. with a given n input by console (n>0). '''
def f(n):
  if n==0:
    return 1
  elif n>0:
    return f(n-1)+100
  else:
    print("The number should be positive")
n=int(input("Enter the number of terms : "))
f(n)