# Write your program here
l=input('gggg')
d=[format((ord(c)+1)<<1,'b') for c in l]
print(' '.join(d))