#!/usr/bin/python

def reverseIndex(l, lidx, hidx):
	sl = l[lidx:hidx+1]
	sl.reverse()

	i = 0
	newl = []

	for elem in l:
		indx = l.index(elem)
		if indx >= lidx and indx <= hidx:
			newl.append(sl[i])
			i += 1
		else:
			newl.append(l[indx])

	return newl

def main():
	#l = reverseIndex([1,2,3,4,5], 1, 3)
	l = reverseIndex(['a', 'b', 'c', 'd', 'e', 'f'], 1, 4)

	print l

if __name__ == "__main__":
	main()
