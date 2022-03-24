#Question 15
'''Write a program which can filter even numbers in a list by using filter function. The list is:
[1,2,3,4,5,6,7,8,9,10]. '''
n=[1,2,3,4,5,6,7,8,9,10]
def f(n):
  if n%2==0:
    return True
  return False
  
m=filter(f,n)

print(list(m))