# Write your program here
def median(mlist:list):
    l=len(mlist)
    if l=0: return 0
    x= sorted(mlist)
    if l%2:
        return x[l//2]
    else:
        return (x[l//2]+x[l//2+1])/2
def mean(mlist:list):
    return sum(mlist)/len(mlist) if mlist else 0
def mode(mlist:list):
    if not mlist: return 0
    d={}
    maxn=0
    for n in mlist:
        if n in d:
            d[n]+=1
        else:
            d[n]=1
        if d[n]>maxn:
            maxn=d[n]
            ni=n

    return ni

def main(mlist:list):
    print(median(mlist))
    print(mean(mlist))
    print(mode(mlist))