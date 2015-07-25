#!/usr/bin/python


test = (1, 2, 3, 4, 5,6)
print test
print 'test[1]', test[1]
print 'test[1:4]', test[1:4]
print 'test[:2]', test[:2]
print 'test[1:]', test[1:]

x = 100
divisors = ()
for i in range(1,x):
	if x%i == 0:
		divisors = divisors + (i,)
		print divisors

sum = 0
for c in str(1957):
	print c
	sum += int(c)
print sum
