#!/usr/bin/python 
# -*- coding: utf-8 -*-
# Author LavaWong
# Date 7/18/2015
# algorithmic complexity
# linear
def exp(x, b):
    if (b == 0):
        return [1, 0]
    crt = 0
    ret = 1
    while b>0:
        crt += 1
        ret = ret*x
        b -= 1
    return [ret, crt]
#linear
def exp1(x, b):
    crt = 1
    if (b == 0):
        return [1, 1]
    if b == 1:
        return [x, 1]
    ret = exp1(x, b-1)
    return [x*ret[0], crt+ret[1]]
#log(n)
def exp2(x, b):
    crt = 1
    if (b == 0):
        return [1, 1]
    if b == 1:
        return [x, 1]
    if b%2 == 0:
        """
        这里进行n/2的出来，指数减半
        """
        ret = exp2(x*x, b/2)
        return [ret[0], crt+ret[1]]
    else:
        ret = exp2(x, b-1)
        return [x*ret[0], crt+ret[1]]
       

def testExp():
    print '%-10s'%'exp(2,4)',exp(2,4)
    print '%-10s'%'exp1(2,4)',exp1(2,4)
    print '%-10s'%'exp2(2,4)',exp2(2,4)
    print '%-10s'%'exp(2,5)',exp(2,5)
    print '%-10s'%'exp1(2,5)',exp1(2,5)
    print '%-10s'%'exp2(2,5)',exp2(2,5)
    print '%-10s'%'exp(2,16)',exp(2,16)
    print '%-10s'%'exp1(2,16)',exp1(2,16)
    print '%-10s'%'exp2(2,16)',exp2(2,16)

testExp()
