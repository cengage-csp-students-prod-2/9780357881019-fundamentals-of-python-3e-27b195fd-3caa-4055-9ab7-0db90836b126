# Write your program here
line=input("Tell me the line")
step=int(input("Tell me the step"))
print(''.join([chr(ord(c)-step) for c in line]))