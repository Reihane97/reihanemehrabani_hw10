import numpy as np
a=np.matrix([[0,0,0,1],[1,0,1,1],[1,0,0,1],[0,0,1,0]])
k=int(input("please enter a number:"))

def func(a,i):
    for j in range(1,i):
        a*=a
    return a
s=np.matrix([[0,0,0,1],[1,0,1,1],[1,0,0,1],[0,0,1,0]])
for i in range (2,k+1):
    mult=func(a,i)
    s+=mult
print(s)
    
