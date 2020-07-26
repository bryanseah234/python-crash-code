import itertools
for a,b,c in itertools.product(itertools.count(0),xrange(0,10),xrange(0,10)):
	print a,b,c
	if a > 20: break
