import math


def test(a):
	if a == 3000:
		return 1
	total = 0
	return math.sqrt(1+(a-1)*test(a+1))


if __name__ == '__main__':
	print (test(2017))