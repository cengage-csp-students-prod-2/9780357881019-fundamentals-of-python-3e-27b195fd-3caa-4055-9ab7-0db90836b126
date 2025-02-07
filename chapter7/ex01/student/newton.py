# Write your code here
TOLERANCE=0.0001
def limitReached (x,appr):
    if abs(x-appr**2)<TOLERANCE: return True
    return False
def improveEstimate(x,estimate):
    return (estimate + x / estimate) / 2
def newton(x:float,estimate:float=1):
    estimate=improveEstimate(x,estimate)
    if limitReached(x,estimate): return estimate
    return newton(x,estimate)
def main():
    x=1
    while x>0:
        x=input("Enter a positive number or enter/return to quit: ")
        if x=="": break
        x=float(x)
        if x<=0: break
        print("The program's estimate is ", newton(x))