#Question 4
#Find whether a given number is an Armstrong number or not
n=int(input("Enter the value = "))
m=n
p=0
order=len(str(n))

for i in range(0,n):
    l=m%10
    p=p+l**order
    m=m//10
if n==p:
    print("Armstrong number")
else:
    print("Not an armstrong number")