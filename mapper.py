#!/usr/bin/env python3

# mapper input
# image  ,location        ,percentage of green in that image
# rh4.jpg,/images/ragihalli,77.81

# mapper output
# key		value
# location	percentage of green in that image	
# ragihalli	77.81

import sys

for line in sys.stdin:

	line = line.strip()
	img_name, img_location, green_perc = line.split(',')
	
	# printing key:value pair 
	results = [img_location[img_location.rfind('/') + 1 :] , str(green_perc)]
	print("\t\t".join(results))

