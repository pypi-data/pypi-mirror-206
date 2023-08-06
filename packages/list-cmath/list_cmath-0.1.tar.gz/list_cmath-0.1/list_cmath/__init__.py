'''
The module does not use python's built-in complex types, but uses lists, such as:
[0.125,0.625] is equivalent to 0.125+0.625i and python complex (0.125+0.625j).
'''

import math
import cmath

def cAdd(a,b):
    '''Returns the sum of two complex numbers'''
    return [a[0]+b[0],a[1]+b[1]]

def cMult(u,v):
    '''Returns the product of two complex numbers'''
    return [u[0]*v[0]-u[1]*v[1],u[1]*v[0]+u[0]*v[1]]

def cPow(x,n):
    '''Returns the n-th power of complex number x'''
    t = x
    for i in range(n-1):
        t = cMult(t,x)
    return t

def magnitude(z):
    '''Return the absolute value of complex number z'''
    return math.sqrt(z[0]**2 + z[1]**2)

'''
If you want to convert between the "list type complex number" used by the module and
the python built-in complex type complex number, please try the following functions:
'''

def listToComplex(z):
    return complex(z[0],z[1])

def complexToList(z):
    return [z.real,z.imag]

def listsToComplexes(lists):
    complexes=[]
    
    for z in lists:
        complexes.append(listToComplex(z))
    
    return complexes

def complexesToLists(complexes):
    lists=[]
    
    for z in complexes:
        lists.append(complexToList(z))
    
    return lists

'''
To operate on a list:
'''
def lcSum(clist):
    '''Returns the sum of one-list of complex numbers'''
    return complexToList(sum(complexesToLists(clist)))

def lcMult(clist):
    '''Returns the product of one-list of complex numbers'''
    s=[1,0]
    
    for z in clist:
        s=cMult(s,z)
    
    return s

def lmagnitude(clist):
    '''Return the absolute value of one-list of complex number'''
    r=[]
    
    for z in clist:
        r.append(magnitude(z))
    
    return r
