#Question 3
#Write a program that accepts a comma separated sequence of words as input and prints the
#words in a comma-separated sequence after sorting them alphabetically
n=input("Enter the sequence of words separated by comma :").split(",")
n.sort()
f = ",".join(n)
print(f)
