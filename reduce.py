# coding: utf-8

import sys

words = {}
for line in sys.stdin:
	word, count = line.split(",")
	try:
		words[word] += int(count)
	except:
		words[word] = int(count)

for word in words.keys():
	print(str(word)+", "+str(words[word]))