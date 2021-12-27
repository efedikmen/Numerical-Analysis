import numpy as np
#actual function f(x)=x-cosx
def fn(x):
    return float(x)-np.cos(x)

#first derivative of f, f'(x)=1+sinx
def fnprime(x):
    return 1.00+np.sin(x)

#Newton's Method
x0=1
tol=0.0005
num=1000
i=0

while i<num:
    x=x0-fn(x0)/fnprime(x0)
    if np.abs(x-x0)<tol:
        print(x)
        i=num+1
    else:
        i+=1
        x0=x