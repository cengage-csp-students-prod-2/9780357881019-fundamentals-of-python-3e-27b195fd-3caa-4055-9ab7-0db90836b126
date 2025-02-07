# Write your code here
TOLERANCE=0.1
def limitReached (x,appr):
    if abs(x-appr**2)<TOLERANCE: return True
    return False
def improveEstimate(x,estimate):
    return (estimate + x / estimate) / 2
def newton(x:float,estimate:float=1):
    estimate=improveEstimate(x,estimate)
    if limitReached(x,estimate): return estimate
    return newton(x,estimate)

x=1
while x>0:
    x=float(input("Enter a positive number or enter/return to quit: ")
    if x<=0: break
    print("The program's estimate is ", newton(x))