#Question 2
#Write a program which can compute the factorial of a given numbers. The results should be
#printed in a comma-separated sequence on a single line
def f(n):
  if n==0:
    return 1
  else:
    return (n*f(n-1))
l=int(input("Enter the starting term :"))
m=int(input("Enter the ending term :"))
k=[]
for i in range(l,m+1):
  k.append(str(f(i)))
print(",".join(k))
