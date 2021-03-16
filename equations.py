 

def ln(x:float):
    yn=0
    i=0
    while i<=100:
        yn1=yn+2*((x-exponent(yn))/(x+exponent(yn)))
        yn=yn1
        i+=1
    return yn1
   
def exponent(x:float):
    if x!=0:
        i=1
        h=1
        b=1
        exp1=0
        while i<=100:
            #mehane
            z=i
            h*=z
            #mone
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
    elif x==0 and y==0:
        return 0
    elif x==0 and y!=0:
        return 0
    elif x<0 and y==0:
        return 1
    else: 
        if y>0:
            i=1
            z1=1
            while i<=y:
                z=z1*x
                z1=z
                i+=1
            return z1
        if y<0:
            i=1
            z1=1
            while i<=(-y):
                z=z1*x
                z1=z
                i+=1
            return 1/z1
  
def sqrt(x:float,y:float):
    if y>=0 and x!=0:
       return XtimesY(y, (1/x))
    elif y<0 or x==0:
        return 0
    elif y==0 and x==0:
        return 0

def calculate(x:float):
    return exponent(x)*XtimesY(7,x)*XtimesY(x,-1)*sqrt(x,x)
   
print(calculate(x))