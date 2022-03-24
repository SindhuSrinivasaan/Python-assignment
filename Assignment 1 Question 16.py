#Question 17
'''Check if a number is present in a list of given numbers and replace the number 
with another number obtained from the user'''
n=input("Enter the list of numbers using comma : ").split(",")
m=input("Enter the number that is present in the list : ")
if m in n:
  print("The number",m,"is present in the index ",n.index(m))
  l=input("Enter the number to replace the given number : ")
  n=str(n)
  j=n.replace(m,l)
  print("The replaced list is ",j)
else:
  print("The number",m,"is not present in the list")