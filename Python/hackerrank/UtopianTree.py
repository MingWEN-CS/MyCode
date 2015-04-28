#!/usr/bin/py

if __name__ == '__main__':
	num = int(raw_input())
	for i in range(0,num):
		cycle = int(raw_input())
		height = 1
		for j in range(0,cycle):
			if (j % 2 == 0):
				height *= 2
			else:
				height += 1
		print height


			
