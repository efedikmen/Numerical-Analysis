#implementation of the power method to find matrix eigenvalues and eigenvectors within a given tolerance level
A = np.array([[-2,1,4],[1,1,1],[4,1,-2]])
x0 = np.array([1,2,-1])
n=2
tol=10**-1000000
num=10000
k=1
p=np.where(x0==abs(x0).max())[0][0]
x0=x0/x0.max()

while k<num:
    y=A@x0
    u=abs(y).max()
    p=np.where(y==u)[0][0]
    if u==0:
        print(x0, "is the eigenvector. A has 0 as an eigenvalue. Select new x0 to restart.")
    err=(x0-(y/y.max())).max()
    x0=y/y.max()
    if err<tol:
        print(x0, "is the eigenvector.", u, "is the eigenvalue.")
    k+=1
    if k==num:
        print(x0, "is the eigenvector.", u, "is the eigenvalue.")
        print("max iter reached")

val,vec = np.linalg.eig(A)

print("Numpy built in fn outputs:")
print("Eigenvalue is", abs(val).max())
print("Eigenvector is", vec[:,np.where(val == val.max())[0][0]])

#inverse power method from the pseudocode in class

q=(x0.T*A@x0)/(x0.T@x0)
k=1
x=x0/x0[np.where(np.abs(x0) == x0.max())]
while k<4:
    D=A-q*np.eye(3)
    y=np.linalg.solve(D,x)
    mu=y[np.where(np.abs(y) == y.max())]
    err=np.abs((x-(y/np.abs(y).max()))).max()
    x=y/mu
    print("Iteration {i}: yp={a}, x={b}, error={c}".format(i=k,a=mu,b=x, c=err))
    k+=1

#Symmetric power method from the pseudocode in class
x=x0/np.linalg.norm(x0,ord=2)
k=1
while k<4:
    y=A@x
    mu=x@y
    normy=np.linalg.norm(y,ord=2)
    if normy==0:
        print("Eigenvalue is 0, select new x")
        
    err=np.linalg.norm(x-(y/normy), ord=2)
    
    x=y/normy
    print("Iteration {i}: yp={a}, x={b}, error={c}".format(i=k,a=mu,b=x, c=err))
    k+=1
