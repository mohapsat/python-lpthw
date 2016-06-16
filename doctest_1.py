import math
import doctest

def addz(a,b):
	"""
	>>> addz(2,3)
	5
	>>> addz(1.4,5.4)
	6.800000000000001
	"""
	return a+b

if __name__ == "__main__":
	doctest.testmod()
