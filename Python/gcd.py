import sys

def gcd(a,b):          
	if (a % b == 0):
		return b
	else:
		return gcd(b, a % b )
	

def main(argv):
	a = int(argv[0])
	b = int(argv[1])
	if (a > b):
		return gcd(a,b)
	else:
		return gcd(b,a)

if __name__ == '__main__':
	print main(sys.argv[1:])