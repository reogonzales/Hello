import numpy as np
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
    if PI_OVR2 <= x < PI:
        res = cosine(x - PI_OVR2)
    elif PI <= x < PI_3OVR2:
        res = - sine(x - PI)
    elif PI_3OVR2 <= x < 2 * PI:
        res = - cosine(x - PI_3OVR2)
    else:
        for i in range(0,10):
             res=res+(pow(-1,i)*pow(x,1+2*i)/factorial(1+2*i))
    return res

def chebyshev(n,x):
    if n==0:
        return 1
    elif n==1:
        return x
    else:
        return 2*x*chebyshev(n-1,x) - chebyshev(n-2,x)

def cheby_zeroes(n):
    nodes=[]
    for i in range(1,n+1):
        nodes.append(cosine(PI*(2*i-1)/(2*n)))
    return nodes


# Press the green button in the gutter to run the script.

#nodes=cheby_zeroes(4)
#print(chebyshev(4,nodes[3]))
#print(round(3.141516,3))

print('=====================')
print("Evaluate cos(x), sine(x) ")
prompt =True
while prompt:
    x=input("Enter x = ")
    if x == '':
        prompt = False
    else:
        x=float(x)
        print( " x = ",x, ": cos(x) = ",cosine(x)," : sin(x) =",sine(x))
        print("sin^2 (x) + cos^2(x) = ", pow(cosine(x),2)+pow(sine(x),2))

#x=[-1,-2,3,4,5,6,7]
#x=np.array(x)
#print( x % 2)
#xa = np.array(x)
#print(cosine(xa))




# See PyCharm help at https://www.jetbrains.com/help/pycharm/
