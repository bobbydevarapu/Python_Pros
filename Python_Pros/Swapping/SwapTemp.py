a=int(input("Enter a : "))
b=int(input("Enter b :"))
print(f"Before swap is : a={a},b={b}")
temp=a
a=b
b=temp
print(temp)
print(f"After swap is : a={a},b={b}")