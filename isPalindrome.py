#!/usr/bin/python
# detect palindrome
def isPalindrome(s):
	if len(s) <= 1:
		return True
	else:
		return s[0] == s[-1] and isPalindrome(s[1:-1]) 


s = str(raw_input('Enter a string: '))
print '\'',s,'\' is ',({True:'', False:'not '}[isPalindrome(s)]),'a palindrome string!'
