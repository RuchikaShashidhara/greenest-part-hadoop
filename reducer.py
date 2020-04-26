#!/usr/bin/env python3

# reducer input
# key		value
# location	percentage of green
# ragihalli	77.81

# reducer output (printing the location in which percentages of green in all the images of that location > 75)
# location
# ragihalli

import sys

last_location = None
count_data = 0
location_count = 0
perc_count_data = 0
green_perc_count = 0
total_locations = 0

for line in sys.stdin:

	line = line.strip()
	location, green_perc = line.split("\t\t")
	
	count_data = 1
	perc_count_data = float(green_perc)
	
	# fist iteration of a key
	if not last_location:
		last_location = location
		
	# nth iteration of the same key
	if location == last_location:
		location_count += count_data
		green_perc_count += perc_count_data	
		
	# first iteration of a different key	
	else:
		# printing the result of the last location if average green_perc > 75
		#result = [last_location, green_perc_count, location_count, round(green_perc_count/ location_count, 2)]
		#print("\t".join(str(v) for v in result))
		if(green_perc_count/location_count > 75):
			print(last_location)
			total_locations += 1
		last_location = location
		location_count = 1
		green_perc_count = float(green_perc)

# printing the result of the last location if average green_perc > 75
#result = [last_location, green_perc_count, location_count, round(green_perc_count/ location_count, 2)]		
#print("\t".join(str(v) for v in result))		
if(location_count != 0 and green_perc_count/location_count > 75):
	print(last_location)	
	total_locations += 1
	print(total_locations)	
	







