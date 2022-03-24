#Question 16
#Print all the occurrences of a number in a given list of numbers 
n=input("Enter the list of numbers using comma : ").split(",")
m=[]
for i in n:
    if i not in m:
        a=n.count(i)
        m.append(i)
        print(i,"count is",a )