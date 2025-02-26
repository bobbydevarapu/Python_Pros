l=list(map(int,input("Enter list: ").split()))
print("List is : ",l)
found=False
for i in l:
  if i%5==0:
    print("This Divisible :",i)
    found=True
if not found:
  print("No number divisible by 5")