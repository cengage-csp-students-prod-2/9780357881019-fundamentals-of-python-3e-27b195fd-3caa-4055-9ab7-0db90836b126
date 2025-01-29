# Write your program here
it=int(input('tell me the number of iterations '))
p=0
sign=1
for i in range(it):
    p+=sign/(1+2*i)
    sign*=-1
print(f'The approximation of pi is {p*4}')