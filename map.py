# coding: utf-8

import sys, re

for line in sys.stdin:

	line = re.sub('[^a-z]', ' ', line.lower())

	words = line.split()
	for word in words:
		print(word + ",1")