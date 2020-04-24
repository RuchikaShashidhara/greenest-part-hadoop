import cv2 
import numpy as np  
import os

def green_prec(image_path):
	img = cv2.imread(image_path)
	#images are converted to 16:9 dimensions
	img = cv2.resize(img, ((800,450)))
	count = 0
	for x in range(800):
		for y in range(450):
			if(img[y,x][1] > img[y,x][2] and img[y,x][1] > img[y,x][2]):
				count += 1
	return str(round(count/3600, 2))

file_data = open("data.txt","w")

images_path = os.getcwd()+'/images'
locations_paths = [x[0] for x in os.walk(images_path)]

for i in range(1, len(locations_paths)):
	location_path = locations_paths[i]
	#location = location_path[len(images_path)+1:]
	for root, direcs, files in os.walk(location_path):
		for filename in files:	
			print(filename)
			print(location_path)
			#print(location)
			print(green_prec(location_path + "/" + filename))	
			file_data.write(filename + "," + location_path + "," + 	green_prec(location_path + "/" + filename) + "\n")	
			print()
	
		

 
   
