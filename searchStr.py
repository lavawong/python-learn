#/usr/bin/python2.7
# -*- coding: utf-8 -*-
import time
"""
n*m 算法
"""
def FoolSearch(oStr, searchStr):
    oLen = len(oStr)
    sLen = len(searchStr)
    if oLen > sLen:
        isSame = False
        for i in range(0, oLen-sLen):
            c = oStr[i]
            j = 0
            if i+sLen > oLen:
                return -1
            elif c == searchStr[j]:
                isSame = True
                for j in range(1, sLen):
                    if oStr[i+j] != searchStr[j]
                        isSame = False
                        break
            if isSame:
                return i
            # return 0 if oStr == searchStr  
            elif oStr == searchStr:
                return 0
    # return -1 if not found
    return -1

"""
KMP算法
"""
def KMPSearch(oStr, searchStr):
    oLen = len(oStr)
    sLen = len(searchStr)
    if oLen > sLen:
        isSame = False
        i = 0
        j = 0
        while i < oLen-sLen and j < sLen:
            if c[i+j] == searchStr[j]:
                i += 1
                j += 1
            else:
                i += 1
                j = 0
        if j == sLen:
            return i - j
    return -1
"""
Boyer-Moore算法
"""
def BMSearch(oStr, searchStr):
    oLen = len(oStr)
    sLen = len(searchStr)
    if oLen > sLen:
        isSame = False
        for i in range(0, oLen-sLen):
            c = oStr[i]
            j = 0
            if i+sLen > oLen:
                return -1
            elif c == searchStr[j]:
                isSame = True
                for j in range(1, sLen):
                    if oStr[i+j] != searchStr[j]
                        isSame = False
                        break
            if isSame:
                return i
            # return 0 if oStr == searchStr  
            elif oStr == searchStr:
                return 0
    # return -1 if not found
    return -1




def testFool():
    oStr = "we are the best! we are the one. I'm going to bead! This is the best algorithm!"
    search = "going"
    index = FoolSearch(oStr, search)
    print 'FoolSearch("%s", "%s") = %d'%(oStr, search, index)

def testKMP():
    oStr = "we are the best! we are the one. I'm going to bead! This is the best algorithm!"
    search = "going"
    index = KMPSearch(oStr, search)
    print 'KMPSearch("%s", "%s") = %d'%(oStr, search, index)

def testBM():
    oStr = "we are the best! we are the one. I'm going to bead! This is the best algorithm!"
    search = "going"
    index = BMSearch(oStr, search)
    print 'BMSearch("%s", "%s") = %d'%(oStr, search, index)
    

def testMultiple():
    ts = time.time()
    for i in range(0, 10**6):
       testFool()
    print "Fool search time:", (time.time() - ts) * 1000

    ts = time.time()
    for i in range(0, 10**6):
       testKMP()
    print "KMP search time:", (time.time() - ts) * 1000

#test()
testMultiple()
    
