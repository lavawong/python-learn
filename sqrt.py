#!/usr/bin/python 
"""
Bi-section method
"""
def sqrtBi(x, epsilon):
    low = 0
    high = max(x, 1)
    crt = 0
    guess = (low + high)/2.0
    val = guess**2 - x
    while abs(val)>epsilon and crt < 100:
       if val < 0:
     low = guess
       else:
     high = guess
       guess = (low + high)/2.0
       val = guess**2 - x
       crt += 1
    
    print 'sqrtBi(',x,',',epsilon,') is', guess, ' count', crt
    return guess if crt < 100 else None


"""
Newton-Raphson method
"""
def sqrtNR(x, epsilon):
    
    crt = 0
    guess = 0.01
    x = float(x)
    if x - 0.0 < epsilon:
       return x
    val = guess**2 - x
    while abs(val)>epsilon and crt < 100:
       guess = guess - val/(2.0*guess)
       val = guess**2 - x
       crt += 1
    
    print 'sqrtNR(',x,',',epsilon,') is', guess, ' count', crt
    return guess if crt < 100 else None
       
def testSqrt():
    sqrtBi(0.25, 0.0001)
    sqrtNR(0.25, 0.0001)

    sqrtBi(1, 0.001)
    sqrtNR(1, 0.001)

    sqrtBi(2, 0.0001)
    sqrtNR(2, 0.0001)

    sqrtBi(2, 0.00001)
    sqrtNR(2, 0.00001)

    sqrtBi(2, 0.0000001)
    sqrtNR(2, 0.0000001)

testSqrt()

