#Question 15
# Check if a number is present in a list of numbers
n=input("Enter the list of numbers using comma : ").split(",")
m=input("Enter the number that is present in the list : ")
if m in n:
  print("The number",m,"is present in the index ",n.index(m))
else:
  print("The number",m,"is not present in the list")