import cv2 
import numpy as np  
import os

def green_prec(image_path):
	
	img = cv2.imread(image_path)
	#images are converted to 16:9 dimensions
	img = cv2.resize(img,(800,450)).tolist()
	
	for x in range(800):
		for y in range(450):
			if(img[y][x][1] > img[y][x][2] and img[y][x][1] > img[y][x][2]):
				img[y][x] = [255, 255, 255]
			else:
				img[y][x] = [0, 0, 0]

	img = np.array(img)
	# Taking a matrix of size 5 as the kernel 

	cv2.imwrite('test.jpg', img)

	img = cv2.imread('test.jpg')

	kernel = np.ones((5,5)) 
	img = cv2.dilate(img, kernel, iterations=1)
	img = img.tolist()

	count = 0
	for i in img:
		for j in i:
			if max(j) > 128:
				count += 1

	
	return str(round(count/3600, 2))

file_data = open("data.txt","w")

images_path = os.getcwd()+'/images'
locations_paths = [x[0] for x in os.walk(images_path)]

for i in range(1, len(locations_paths)):
	location_path = locations_paths[i]
	location = location_path[len(images_path)+1:]
	img_location = "/images/" + location
	for root, direcs, files in os.walk(location_path):
		for filename in files:	
			print(filename)			
			print(img_location)
			print(green_prec(os.getcwd() + img_location + "/" + filename))
			file_data.write(filename + "," + img_location + "," + 	green_prec(os.getcwd() + img_location + "/" + filename) + "\n")	
			print()
			
file_data.close()