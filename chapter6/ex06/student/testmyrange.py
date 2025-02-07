# Write your code here
def myRange(start:int,stop:int=None,step:int=None)
    if stop is None:
        if step<0 and start>0:
            stop=0
        start,stop=0,start
    if step is None or step=0:
        step=1
    l=[]
    pos=start
    if step>0:
        while pos<stop:
            l.append(pos)
            pos+=step
    else:
        while pos>stop:
            l.append(pos)
            pos+=step
    return l