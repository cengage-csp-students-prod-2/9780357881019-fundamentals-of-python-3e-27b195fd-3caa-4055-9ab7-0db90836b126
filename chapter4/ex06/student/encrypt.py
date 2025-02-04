# Write your program here
l=input('gggg')
l=[format((ord(c)+1)<<1,'b') for c in l]
print(' '.join(l))