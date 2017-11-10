#!/usr/bin/python

def multiply(a):
	prev = 1
	last = 1
	
	for i in range(0, len(a)):
		temp = a[i]
		if i == len(a)-1:
			a[i] = prev * last
		else:
			a[i] = prev * a[i+1]
		prev = temp

	return a
		
def main():
	a = [2, 3, 4, 5, 6]
	b = multiply(a)

	print b

if __name__ == "__main__":
	main()
