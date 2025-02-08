# Write your code here
seq=[1,2,3,4,5,6]
def printAll(seq):
    if seq:
        #print(seq[0])
        print(seq)
        printAll(seq[1:])
printAll(seq)
print(seq)