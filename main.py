import numpy as np
import scipy.linalg as la
import math
PI = math.pi
PI_OVR2   = 0.5*PI
PI_3OVR2  = 1.5*PI

def factorial(n):
    res=1
    for i in range(1,n+1):
        res=res*i
    return res

def cosine(x):
    res = 1
    x = x % (2*PI)
    if PI_OVR2 <= x < PI:
        res = -sine(x-PI_OVR2)
    elif PI <= x < PI_3OVR2:
        res = - cosine(x - PI)
    elif PI_3OVR2 <= x < 2*PI:
        res = sine(x-PI_3OVR2)
    else:
        for i in range(1,10+1):
            res=res+(pow(-1,i)*pow(x,2*i)/factorial(2*i))
    return res

def sine(x):
    res=0
    x = x % (2 * PI)
    if PI_OVR2 <= x < PI:         #2nd Quadrant
        res = cosine(x - PI_OVR2)
    elif PI <= x < PI_3OVR2:      #3rd Quadrant
        res = - sine(x - PI)
    elif PI_3OVR2 <= x < 2 * PI:  #4th Quadrant
        res = - cosine(x - PI_3OVR2)
    else:                         #1st Quatrant
        for i in range(0,10):
             res=res+(pow(-1,i)*pow(x,1+2*i)/factorial(1+2*i))
    return res

def chebyshev(n,x):
    if n==0:
        return np.ones(x.size)
    elif n==1:
        return x
    else:
        return 2*x*chebyshev(n-1,x) - chebyshev(n-2,x)

def chebyshevAll(n,x):
    if n==0:
        return 1
    elif n==1:
        return x
    else:
        r=[]
        for i in range(0,n):
            r.append(chebyshev(i,np.array([x])))
        return np.array(r)

def cheby_zeroes(n):
    nodes=[]
    for i in range(1,n+1):
        nodes.append(cosine(PI*(2*i-1)/(2*n)))
    return np.array(nodes)

def funX(x):
#    return np.array(2*pow(x,4)+1)
    return np.array(2*pow(x,3)-2)

#print('=====================')
#print("Evaluate cos(x), sine(x) ")
# prompt =True
# while prompt:
#     x=input("Enter x = ")
#     if x == '':
#         prompt = False
#     else:
#         x=float(x)
#         print( " x = ",x, ": cos(x) = ",cosine(x)," : sin(x) =",sine(x))
#         print("sin^2 (x) + cos^2(x) = ", pow(cosine(x),2)+pow(sine(x),2))

print("==========================")
print("Chebyshey Discretization:")
#   f(x) = a0*T0(x) + a1*T1(x) + a2*T2(x) + ... + an*Tn(x)  where x are roots of Tn(x)
#   [ f(x1), f(x2), ...,f(xn)] = b  =  t * a       solve for a=[a1,a2,...an]
prompt=True
while prompt:
    nodeSize=input("Enter number of nodes = ")
    if nodeSize== '':
        prompt=False
    else:
        nodeSize=int(nodeSize)
        nodes=cheby_zeroes(nodeSize)
        fAtNodes = funX(nodes)    # b

        t = np.array(chebyshev(0,nodes))
        for i in range(1,nodeSize):
            t = np.column_stack((t,chebyshev(i,nodes)))
        a = np.linalg.solve(t,fAtNodes)
        print("f(x) ~ a * T(x) = a0*T0(x) + a1*T1(x) + ... + an * Tn(x)")
        print("a = " ,a)
        valPrompt=True
        while valPrompt:
            xval=input("Evaluate at x =")
            if xval== '':
                valPrompt=False
            else:
                xarg=float(xval)
                val = funX(xarg)
                val2 = chebyshevAll(nodeSize,xarg)
                print(np.dot(a,val2))
                print(val)
        #nodesVal=np.array(chebyshev(nodeSize,nodes))
        #print(np.column_stack((nodes,nodesVal,funX(nodes))))
        #a = np.array([[1,2,3],
        #             [0,5,0],
        #             [10,1,1]])
        #b = np.array([1,2,3])
        #x = np.linalg.solve(a,b)
        #print(x)
        #print(np.dot(a,x))

