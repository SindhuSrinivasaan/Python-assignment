#Question 17
'''Write a program which can map() and filter() to make a list whose elements are square of even
number in [1,2,3,4,5,6,7,8,9,10]. '''
n=[1,2,3,4,5,6,7,8,9,10]
f=filter(lambda x: x%2==0,n)
l=list(f)
m=map(lambda x: x*x,l)
print(list(m))