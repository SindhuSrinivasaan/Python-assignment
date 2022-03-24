#Question 10
#Check whether a given word is a palindrome or not
'''n=input("Enter a word = ")
s=n[::-1]
if n==s:
    print("Palindrome")
else:
    print("It is Not Palindrome")'''

n=input("Enter a word = ")
k=[]
for i in n:
    k.insert(0,i)
print("".join(k))