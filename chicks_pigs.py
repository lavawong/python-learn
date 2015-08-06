#!/usr/bin/python

# Compute the number of pigs and chicks
def solve(legs, heads):
    # check pig and chicks
    if heads*4 >= legs and legs >= heads: 
        pigNum = 0
    for pigNum in range(0, heads+1):
        # pig has 4 legs and chick has 2
        if 4*pigNum+2*(heads-pigNum) == legs:
            return [pigNum, heads-pigNum]
        # if pigNum is equal heads and legs larger than given legs it's error
        if pigNum == heads and 4*pigNum != legs:
            print 'Some of lame pigs or chicks in them!'
    return [None, None]
       

def barnYard():
    legs = int(raw_input('Enter legs: '))
    heads = int(raw_input('Enter heads: '))
    pigNum, chickNum = solve(legs, heads)
    if pigNum != None:
        print 'There are ', pigNum, ' pigs and ', chickNum, 'chicks'
    else:
        print 'You enter the wrong legs and heads'

barnYard()
