#Question 18
#Write a program to compute 1/2+2/3+3/4+...+n/n+1 with a given n input by console (n>0). 
n=int(input("Enter the number of terms : "))
l,s=[],0
if n>0:
  for i in range(1,n+1):
    m=str(i)+"/"+str(i+1)
    l.append(m)
    s+=i/(i+1)
else:
  print("The number should be positive")
m="+".join(l)
print("The value of",m,"is :",round(s,2))