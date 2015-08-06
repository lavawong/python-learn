#!/usr/bin/python 
# Author LavaWong
# Date   7/13/2015 
import math
# Syntax learn
# compute triangle hypotenuse
def computeHyp(base, height):
    return math.sqrt(base**2 + height**2)

def getFloat(name):
    inputOK = False
    while not inputOK:
        try:
            base = raw_input("Enter "+name+": ")
            inputOK = (type(1.0) == type(float(base)))
            if inputOK:
                break
            else:
                print 'Input error number'
        except Exception as e:
            print 'input error ',e
    return base
    
def testHyp():
    
    base = getFloat('base')
    height = getFloat('height')
    hyp = computeHyp(float(base), float(height))
    print 'Hypotenuse is', hyp

testHyp()
