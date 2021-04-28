#!/usr/bin/python3
def uppercase(str):
	for charz in str:
		if charz not in 'abcdefghijklmnopqrstuvwxyz':
			out = out + charz
		else:
			k = ord(charz)
			l = k - 32
			out = out + chr(l)
print('', out)