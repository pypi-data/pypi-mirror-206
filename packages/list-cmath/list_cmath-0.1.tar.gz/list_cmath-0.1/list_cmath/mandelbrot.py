from myMaths.cmath.basic import *

def mandelbrot(z,num):
    '''Run the process num times and
    return the number of diverging times'''
    count=0
    # Assign the value of z to z1
    z1=z
    # Iteration num times
    while count <=num:
        # Check for divergence
        if magnitude(z1) > 2.0:
            # Returns the number of iterations at divergence
            return count
        # Calculate new z1
        z1=cAdd(cMult(z1,z1),z)
        count+=1
    # If it does not diverge in the end
    return num

def mandelbrot_p(z,num,n):
    '''Run the process num times and
    return the number of diverging times'''
    count=0
    # Assign the value of z to z1
    z1=z
    # Iteration num times
    while count <=num:
        # Check for divergence
        if magnitude(z1) > 2.0:
            # Returns the number of iterations at divergence
            return count
        # Calculate new z1
        z1=cAdd(cPow(z1,n),z)
        count+=1
    # If it does not diverge in the end
    return num

def mandelbrot_e(z,num,a):
    '''Run the process num times and
    return the number of diverging times'''
    count=0
    # Assign the value of z to z1
    z1=z
    # Iteration num times
    while count <=num:
        # Check for divergence
        if magnitude(z1) > 2.0:
            # Returns the number of iterations at divergence
            return count
        # Calculate new z1
        z1=cAdd(eval(a),z)
        count+=1
    # If it does not diverge in the end
    return num
