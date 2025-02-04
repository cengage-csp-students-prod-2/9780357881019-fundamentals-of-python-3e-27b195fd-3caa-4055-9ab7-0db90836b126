# Write your program here
l=input('gggg')
d=[str(format((ord(c)+1)<<1,'b')) for c in l]
print(' '.join(d))