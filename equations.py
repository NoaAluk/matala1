
def ln(x:float):
    yn=x-1.0
    yn1=0
    a=yn-yn1
    if a<0:
        a=a*(-1)
    while a>0.001:
        yn1=yn+2*((x-exponent(yn))/(x+exponent(yn)))
        a=yn-yn1
        if a<0:
            a=(-1)*a
        yn=yn1
    return yn1


def exponent(x:float):
    if x!=0:
        i=1
        h=1
        b=1
        exp1=0
        while i<=100:
            z=i
            h*=z
            a=x
            b=b*a
            exp=b/h
            exp1+=exp
            i+=1
        return exp1+1
    else:
        return 1

def XtimesY(x:float,y:float):
    if x>0:
        z=y*ln(x)
        return exponent(z)
    elif x<0 and y==0:
        return 1
    else: return 0
  

def sqrt(x:float,y:float):
    if y>=0 and x!=0:
       return XtimesY(y, (1/x))
    else:
        return 0


def calculate(x:float):
    return exponent(x)*XtimesY(7,x)*XtimesY(x,-1)*sqrt(x,x)
