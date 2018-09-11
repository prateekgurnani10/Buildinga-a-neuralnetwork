import numpy as np
import matplotlib.pyplot as plt

X,y = np.loadtxt('x03.txt',delimiter=',',unpack = True)



data= np.genfromtxt('x03.txt',delimiter=',')


def normalEquation(X,y):
    m = int(np.size(data[:,1]))
    
    w = []
    
    bias_vector = np.ones((m,1))
    
    X= np.reshape(X,(m,1))
    
    X = np.append(bias_vector, X, axis=1)
    
    
    X_transpose = np.transpose(X)
    
    
    w = np.linalg.inv(X_transpose.dot(X))
    w = w.dot(X_transpose)
    w = w.dot(y)
    
    return w

[p0,p1] = normalEquation(X,y)
xx = np.linspace(20,70)
yy = p0 + p1 * xx
print(p1,p0)
plt.scatter(X,y)
plt.plot(X,y,'bo')
plt.plot(xx,yy)











