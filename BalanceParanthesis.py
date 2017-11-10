#!/usr/bin/python

from ds.Stack import *

def isMatch( sP, cP ):
	if ((sP == "{" and cP == "}") or (sP == "[" and cP == "]") or (sP == "(" and cP == ")")):
		return True
	
	return False

def isBalanced(exp):
	if exp is None or exp == "":
		return False

	s = Stack()
	for char in exp:
		if char == "{" or char == "[" or char == "(":
			s.push(char)
		elif char == "}" or char == "]" or char == ")":
			try:
				stkChar = s.pop()
				if not isMatch(stkChar, char):
					return False
			except Exception as e:
				print ("Exception:", e)
				return False
		else:
			continue

	# Check that stack is empty at this point
	if not s.isEmpty():
		return False

	return True

def main():
	#exp = "aernawejbasdahnwaawej"
	exp = "{aern{awejb[asd]}ahnwa(awej)}"
	print (isBalanced(exp))

if __name__ == "__main__":
	main()
