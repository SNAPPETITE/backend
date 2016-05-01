#Tests the pictures using sample group.
#author: Henry Woo <hcwoo2>

from PIL import Image
import numpy as np
import csv
from sklearn.svm import SVC

with open('RGBValue.csv','rb') as f:
	reader = csv.reader(f)
	RGBValue = list(reader)

with open('foodNames.csv','rb') as f:#import array
	reader = csv.reader(f)
	foodNameTemp = list(reader)

foodName = []
for i in foodNameTemp:
	foodName += i

X = np.array(RGBValue)
y = np.array(foodName)

clf = SVC()
clf.fit(X,y)

food = raw_input("Enter image file name here.\n")
food = Image.open(food)
food = np.asarray(food)
average = [0,0,0]
numOfValues = 0
for i in food:
	for j in i:
		if (j[0] + j[1] + j[2] != 0) or (j[0] + j[1] + j[2] != 765): 
		#ignore transparent pixels and white pixels
			average[0] += j[0]
			average[1] += j[1]
			average[2] += j[2]
			numOfValues += 1

for i in xrange(0,3):
	average[i] = average[i] / numOfValues

total = float((average[0] + average[1] + average[2]))

for i in xrange(0,3):
	average[i] = average[i] / total

print average
print(str(clf.predict([average])))

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
	
	ax.scatter(average[0], average[1], average[2], c = 'r', marker = 'x', label = 'Your Food')#plot the food that was given

	ax.set_xlabel('Red')#set axis labels
	ax.set_ylabel('Green')
	ax.set_zlabel('Blue')

	#position legend
	plt.legend(loc='upper left', numpoints=1, ncol=3, fontsize=8, bbox_to_anchor=(0, 0))

	plt.show()#display graph

	showGraph = False
