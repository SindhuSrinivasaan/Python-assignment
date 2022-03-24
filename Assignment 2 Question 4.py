#Question 5
#Write a program that accepts a sequence of whitespace separated words as input and prints the
#words after removing all duplicate words and sorting them alphanumerically
n=input("Enter the sequence of words separated by whitespace :").split(" ")
m=[]
n.sort()
for i in n:
  if i not in m:
    m.append(i)
  else:
    continue
f= " ".join(m)
print(f)