#Adds to the sample group
#Author: Henry Woo <hcwoo2>

from PIL import Image
import numpy as np
import csv


filename = raw_input("Enter filename with extension.\n")
temp = Image.open(filename)
maxsize = (640, 640)
temp = temp.resize(maxsize, Image.ANTIALIAS)#shrink image
temp = np.asarray(temp)#array to extract features

foodName = raw_input("Enter the name of the food.\n")#pairs with name
foodName = [foodName]

print "Array is named 'temp'"


average = [0,0,0]
numOfValues = 0
for i in temp:
	for j in i:#for each set of RGB values
		if ((j[0] + j[1] + j[2]) > 50) or ((j[0] + j[1] + j[2]) < 700): 
		#ignore transparent pixels and white pixels
			average[0] += j[0]
			average[1] += j[1]
			average[2] += j[2]
			numOfValues += 1

for i in xrange(0,3):
	average[i] = average[i] / numOfValues

total = float((average[0] + average[1] + average[2]))

for i in xrange(0,3):
	average[i] = average[i] / total#make the averages a ratio

print "RGB average is: " + str(average)

with open("RGBValue.csv", "a") as fp:
	wr = csv.writer(fp, dialect='excel')
	wr.writerow(average)

with open('foodNames.csv' , 'a') as fn:
	wr = csv.writer(fn, dialect='excel')
	wr.writerow(foodName)




####################################
########## 3D Graphing #############
####################################

showGraph = raw_input('Show graph? [y/n]\n')
status = True
while(status):
	showGraph.lower()#case insensitive
	if showGraph == 'y':
		showGraph = True
		status = False
	elif showGraph == 'n':
		showGraph = False
		status = False
	else:
		showGraph = raw_input('Invalid input, show graph? [y/n]\n')

while(showGraph):
	import matplotlib.pyplot as plt
	from mpl_toolkits.mplot3d import Axes3D
	fig = plt.figure()
	ax = fig.add_subplot(111, projection = '3d')

	with open('RGBValue.csv','rb') as f:
		reader = csv.reader(f)
		RGBValue = list(reader)

	with open('foodNames.csv','rb') as f:
		reader = csv.reader(f)
		foodNameTemp = list(reader)

	foodName = []
	for i in foodNameTemp:
		foodName += i

	pairList = zip(foodName,RGBValue)#pair foods with their values

	colorMap = {}#assign each food its own color

	for i in pairList:
		if (i[0] not in colorMap):
			colorMap[i[0]] = [[np.random.rand()],[np.random.rand()],[np.random.rand()]]#set a random color to each food


	for i in pairList:
		x = float(i[1][0])
		y = float(i[1][1])
		z = float(i[1][2])
		ax.scatter(x, y, z, c = colorMap[i[0]], label = i[0])#plot on 3d graph
	

	ax.set_xlabel('Red')#set axis labels
	ax.set_ylabel('Green')
	ax.set_zlabel('Blue')

	#position legend
	plt.legend(loc='upper left', numpoints=1, ncol=3, fontsize=8, bbox_to_anchor=(0, 0))

	plt.show()#display graph

	showGraph = False
