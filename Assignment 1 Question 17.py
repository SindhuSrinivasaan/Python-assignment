#Question 18
#Replace a word in the given line of text with another word
n=input("Enter the line of text : ")
m=input("Enter the word to be replace :")
for i in n.split():
  if i==m:
    l=input("Enter the replacing word :")
    k=n.replace(m,l)
    print("The replaced text is",k)
if i!=m:
  print("The word is not in text")
