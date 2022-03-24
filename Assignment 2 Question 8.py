#Question 8
#Write a program that accepts a sentence and calculate the number of letters and digits. 
n=input("Enter a sentence : ")
l,d=0,0
for i in n:
  if i.isalpha():
    l+=1
  elif i.isnumeric():
    d+=1
print(l,d)
