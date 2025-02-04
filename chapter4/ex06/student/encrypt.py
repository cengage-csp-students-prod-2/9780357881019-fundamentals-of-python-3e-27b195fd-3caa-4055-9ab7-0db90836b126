# Write your program here
l=input('gggg')
d=[format((ord(c)+1),'b') for c in l]
d=[c[1:]+c[0] for c in d]
print(' '.join(d))