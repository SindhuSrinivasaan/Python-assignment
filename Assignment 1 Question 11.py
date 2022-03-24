#Question 11
#Print the number of vowels and consonants in a given word
n=input("Enter a word = ")
v=0
c=0
vowels=['a','e','i','o','u','A','E','I','O','U']
for i in n:
    if i in vowels:
        v=v+1
    else:
        c=c+1
print(v,c)