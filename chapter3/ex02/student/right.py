# Write your program here
print('Hello')
a=float(input("enter side 1"))
b=float(input("enter side 2"))
c=float(input("enter side 3"))
sides=[a,b,c].sort()
print("The triangle is a right triangle." if a**2+b**2==c**2 else "The triangle is not a right triangle.")