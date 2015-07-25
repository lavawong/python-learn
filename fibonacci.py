#!/usr/bin/python
# fibonacci function
numCalls = 0
def fibFast(n, men):
	global numCalls
	numCalls += 1
	#print 'numCalls:', numCalls
	if not n in men:
		men[n] = fibFast(n-1, men) + fibFast(n-2, men)
	return men[n]
	
def fib(n):
	men = {0:0, 1:1}
	if n == 0 or n == 1: 
		return 1
	else: 
		return fibFast(n, men)


n = int(raw_input('Enter a number: '))
print 'n is:', n, 'fast fib:',fib(n), ' calls:', numCalls
