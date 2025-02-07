def myRange(start:int,stop:int=None,step:int=None):
    if step is None or step==0:
        step=1
    if stop is None:
        if step<0 and start>0:
            stop=0
        start,stop=0,start

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

def main():
    print(myRange(10))
    print(myRange(1, 10))
    print(myRange(1, 10, 2))
    print(myRange(10, 1, -1))

main()