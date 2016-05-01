#Tests the pictures using sample group.
#author: Henry Woo <hcwoo2>

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