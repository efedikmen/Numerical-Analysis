import numpy as np
import pandas as pd
def reg(a):#takes np.matrix as input
    rows, cols = a.shape
    A = np.empty((rows,3))
    y = np.empty(rows)
    #creates the A matrix from the input
    for i in range(rows):
            A[i,0]=1
            A[i,1]=a[i,0]
            A[i,2]=(a[i,0])**2
            y[i]=a[i,1]
    #qr decomposition
    Q,R= np.linalg.qr(A)
    res=np.dot(Q.T,y)
    x = np.linalg.solve(R, res)
    pred = np.dot(x.T,A.T)
    results = pd.DataFrame(data={"t":range(1,rows+1),
                "predictions":pred,"actual values":y})
    
    return x,results

#our actual matrix
a=np.matrix([[1,14],[2,20],[3,21],[4,24],[5,15],[6,45],[7,67],[8,150],[9,422],[10,987]])
x,df=reg(a)

ax1 = df.plot(kind='scatter', x='t', y='actual values', color='r')    
ax2 = df.plot(kind='scatter', x='t', y='predictions', color='g',
              title="Equation:{a}+{b}t+{c}t^2 (Greens are predictions)".format(a=x[0],b=x[1],c=x[2]), ax=ax1)     