# Write your program here
print('Hello')
a=float(input("enter side 1"))
b=float(input("enter side 2"))
c=float(input("enter side 3"))
sides=sorted([a,b,c])
print("The triangle is a right triangle." if sides[0]**2+sides[1]**2==sides[2]**2 else "The triangle is not a right triangle.")