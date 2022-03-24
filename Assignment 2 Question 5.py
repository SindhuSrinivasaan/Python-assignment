#Question 6
#Write a program which accepts a sequence of comma separated 4-digit binary numbers as its
#input and then check whether they are divisible by 5 or not. The numbers that are divisible by 5 are
#to be printed in a comma separated sequence.
n=input("Enter 4-digit binary numbers separated by comma :").split(",")
k=[]
for i in n:
  m=list(i)
  s=0
  for j in range(len(m)):
      l=m.pop()
      if l=="1":
        s+=2**j
  if s%5==0:
    k.append(i)
print(",".join(k))