#!/usr/bin/python
# -*- coding: utf-8 -*-
# 记录调用次数
numCalls = 0

# 快速算法, 空间换时间 dynamic algorithm
def fibFast(n, men):
    global numCalls
    numCalls += 1
    #print 'numCalls:', numCalls
    if not n in men:
       men[n] = fibFast(n-1, men) + fibFast(n-2, men)
    return men[n]
    
# fibonacci function
def fib(n):
    men = {0:0, 1:1}
    if n == 0 or n == 1: 
       return 1
    else: 
       return fibFast(n, men)

try:
    n = int(raw_input('Enter a number: '))
    print 'n is:', n, 'fast fib:',fib(n), ' calls:', numCalls
except Exception as e:
    print 'Input Error:',e
