#Question 3
#Demonstrate the usage of break, continue and pass statements. 

#Using break
s = "1234554321"
print("Break will stop at 4")
for i in s:
    if i == "4":
        break
    print(i,end="")
  
print("\n")
#Using continue
print("Continue will skip 4")
for i in s:
    if i == "4":
        continue
    print(i,end="")

print("\n")
#Using pass
print("Pass will pass to next step ")
for i in s:
    if i == "4":
        pass
    print(i,end="")