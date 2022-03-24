#Question 13
#Print the number of letters, digits, whitespace characters, newline characters in a given text
n=input("Enter a line of text : ")
a,b,c,d=0,0,0,0

if "\\n" in n:
    f=n.replace("\\n","!")
for i in f:
    if i.isalpha():
        a+=1
    elif i.isnumeric():
        b+=1
    elif (i==" "):
        c+=1
    elif i=="!":
        d+=1

print("Number of letters in the given text is ",a)
print("Number of digits in the given text is ",b)
print("Number of whitespace characters in the given text is ",c)
print("Number of newline characters in the given text is ",d)