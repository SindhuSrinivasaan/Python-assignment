#Question 20
#Write a program to generate a list with 5 random numbers between 100 and 200 inclusive. 
import random
l=[]
for i in range(5):
  n=random.randint(100,201)
  l.append(n)
print(l)