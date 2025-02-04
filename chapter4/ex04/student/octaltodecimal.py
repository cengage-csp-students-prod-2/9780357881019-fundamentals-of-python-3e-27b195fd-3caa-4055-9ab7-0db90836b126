# Write your program here
inf=input("input file")
inf=list(inf)
n=0
m=1
while inf:
    n+=int(inf.pop())*m
    m*=8
print(n)
#outf=input("outputfile")
#with open(inf, 'r') as f:
#    line=int(f.read())
#with open(outf,'w') as f:
#    f.write(format(line,'o'))
#print(format(int(inf),'o'))