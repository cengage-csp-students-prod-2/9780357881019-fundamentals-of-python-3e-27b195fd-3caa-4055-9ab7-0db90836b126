# Write your program here
infname=input("input file")
outf=input("outputfile")
with open(infname, 'r') as f:
    line=int(f.read())
with open(outf,'w') as f:
    f.write(format(line,'o'))