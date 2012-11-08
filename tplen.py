#!/usr/bin/python
# -*- coding: utf-8 -*- 
from math import fsum

data = { 
	'10m':	[  1.25, 1.12, 1.36, 1.42, 1.39, 1.06, 1.28, 1.08, 1.63, 2.04 ],
	'14m':	[ 1.54, 1.45, 1.84, 1.53, 1.55, 1.52 ],
	'33m':	[ 3.42, 3.14, 3.50 ]
	}

result = {}

for length, ohms in data.items():
	sum = 0
	l = int( length[0:-1] )
	print ("calculating for length: %d"  % l)
	
	for i, ohm in enumerate(ohms):
		sum = sum +  l/ float( ohm )
	
	result[length] = float(sum) / i

print "The average distributed by cable length is: "
print result

er = fsum( result.itervalues() ) / len(result)
print "The average overall konstant er[m/Ω] is: er = %s" % er



