# Write your program here
def median(mlist:list):
    return sorted(mlist)[len(mlist)//2] if mlist else 0
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