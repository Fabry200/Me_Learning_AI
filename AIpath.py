import numpy as np
import math
from sympy import *
from sympy.abc import x,y
import time

x0=np.random.randint(0,9999,(1))
y0=np.random.randint(0,9999,(1)) #parameter x and y
x1=np.random.randint(0,9999,(1))
y1=np.random.randint(0,9999,(1))
print("Points x:",x0,"y:",y0," ","x1:",x1," ","y1:",y1)

dx=Eq(((x-x0[0])/(x1[0]-x0[0]))-((y-y0[0])/(y1[0]-y0[0])),0)
fy=solve(dx,y)

print("f(x)=",fy)

#weights
a=np.random.randn()
b=np.random.randn()
c=np.random.randn()
d=np.random.randn()


learning_rate=1e-6

### sempre dichiarare i gradienti prima
grad_a=0
grad_b=0
grad_c=0
grad_d=0
dxpred=0
grad_dx=0

tempo=time.time()
for g in range(200000):
    xp=a
    yp=b
    x1p=c
    y1p=d
    grad_x_perd=200*(xp-x0)
    grad_y_perd=200*(yp-y0)
    grad_a=grad_x_perd.sum()
    grad_b=grad_y_perd.sum()
    a -= learning_rate*grad_a
    b -= learning_rate*grad_b
    grad_z_perd=200*(x1p-x1)
    grad_e_perd=200*(y1p-y1)
    grad_c=grad_z_perd.sum()
    grad_d=grad_e_perd.sum()
    c -= learning_rate*grad_c
    d -= learning_rate*grad_d

xp=int(round(xp,0))
yp=int(round(yp,0))
x1p=int(round(x1p,0))
y1p=int(round(y1p, 0))
fine=time.time()
        #dfypred=dfypred-(learning_rate*grad_dx)

dxpred=Eq(((x-xp)/(x1p-xp))-((y-yp)/(y1p-yp)),0)
fypred=solve(dxpred,y)
print("Points calculated: x:",xp,"y:",yp," ","x1:",x1p," ","y1:",y1p)
print("Calculated f(x)=",fypred,"Exec time: ",fine-tempo)
