#Question 12
#Define a function that can accept two strings as input and print the string with maximum length in console.
def f(n,m):
  if len(n)>len(m):
    return n
  elif len(n)==len(m):
    return ("Equal")
  else:
    return m
n=input("Enter the first string : ")  
m=input("Enter the second string : ") 
print(f(n,m))
