#Question 19
#Replace a given letter in the line of text with another letter of users choice
n=input("Enter a line of text : ")
m=input("Enter the letter that is present in the text : ")
l=input("Enter the letter to replace : ")
j=n.replace(str(m),str(l))
print("The replaced text is ",j)