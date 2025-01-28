# Write your program here
print('Hello')
a=float(input("enter side 1"))
b=float(input("enter side 2"))
c=float(input("enter side 3"))
sides=[a,b,c].sorted()
print(True if a**2+b**2==c**2 else False)