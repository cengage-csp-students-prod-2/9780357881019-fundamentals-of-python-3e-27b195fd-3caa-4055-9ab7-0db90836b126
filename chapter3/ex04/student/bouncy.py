# Write your program here
a=float(input("Enter the height from which the ball is dropped: "))
bi=float(input("Enter the bounciness index of the ball: "))
n=float(input("Enter the number of times the ball is allowed to continue bouncing: "))
d=a*(1-bi**n)/(1-bi)*(1+bi)
print(f'Total distance traveled is: {d} units.')