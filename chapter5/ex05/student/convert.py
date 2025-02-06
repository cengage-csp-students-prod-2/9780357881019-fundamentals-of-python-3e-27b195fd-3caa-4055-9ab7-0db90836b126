# Write your program here
DIGITS={}
for i in range(10): DIGITS[i]=i
for i in range(26): DIGITS[chr(65+i)]=i+10
def repToDecimal (rep,base):
    rep2=rep.upper()
    l=list(rep)
    n=0
    m=1
    while l:
        n+=DIGITS[l.pop()]*m
        m*=base
    return n
def main(s,b):
    print(repToDecimal(s,b))