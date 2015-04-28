#!/usr/bin/py

if __name__ == '__main__':
	n = int(raw_input())
	for i in range(0,n):
		string = raw_input()
		ans = 0
		for j in range(0,len(string)-1):
			if string[j] == string[j+1]:
				ans += 1
		print ans
	
