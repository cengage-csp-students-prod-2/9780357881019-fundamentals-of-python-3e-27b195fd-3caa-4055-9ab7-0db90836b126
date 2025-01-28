# Write your program here
a=float(input("Enter the height from which the ball is dropped: "))
bi=float(input("Enter the bounciness index of the ball: "))
n=float(input("Enter the number of times the ball is allowed to continue bouncing: "))
d=a*bi**n+a*bi**(n-1)
print(f'Total distance traveled is: {d} units.')