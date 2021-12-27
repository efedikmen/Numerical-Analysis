import numpy as np
import matplotlib.pyplot as plt

#the actual f function
def f(x):
    if x >= 0:
        return 1
    else: 
        return -1

#function evaluates the Lagrange polynomial using the specified number of nodes   
def interpoly(pts):
    #generating equidistant specified number of nodes in the interval [-1,1]
    x=np.linspace(-1,1,num=pts)
    #values of f corresponding to the nodes
    y=np.array([f(i) for i in x])
    
    #generating points to graph
    graphx=np.arange(-1,1,0.1)
    graphy = np.zeros(graphx.size)
    
    #the loop evaluates the Lagrange polynomial for all generated points
    for a in range(graphx.size):
        for i in range(pts):
            elem=y[i]
            for j in range(pts):
                if i!=j:
                     elem=elem*(graphx[a]-x[j])/(x[i]-x[j])   
            graphy[a]+=elem
    #actual 
    fy=np.array([f(i) for i in graphx])
    
    #absolute value of the error at each point
    err=np.abs(fy-graphy)
    
    #outputs the x values, the poly approx values, actual values, and the error
    return [graphx,graphy,fy,err]

    #plotting f(x) vs p(x)
fig, ax = plt.subplots(figsize=(8, 4))
ax.plot(interpoly(8)[0], interpoly(8)[1],label="approx")
ax.plot(interpoly(8)[0], interpoly(8)[2],label="actual")
plt.legend()
plt.title("Actual vs Approx Using 8 Interpolation Points")
plt.show()

#plotting the error function
fig, ax = plt.subplots(figsize=(8, 4))
ax.plot(interpoly(8)[0], np.log(interpoly(8)[3]))
plt.title("Error Function in Log Scale Using 8 Interpolation Points")
plt.show()

#Plotting the error functions for polynomials with more interpolation points
fig, ax = plt.subplots(figsize=(8, 4))
for i in [16,32,64,128,256]:
    ax.plot(interpoly(i)[0], np.log(interpoly(i)[3]),label="{x} points".format(x=i))
plt.title("Error Function in Log Scale Using Varying Interpolation Points")
plt.legend()
plt.show()
