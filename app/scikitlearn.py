from sklearn import linear_model
from PIL import Image
#probably wanna make a whole program to scrape the image for the different sections
#which have food on the plate and then save each section as its own class with rgb values.
#But I just figured scrambled eggs are yellow (255,255,0) so heres a small program 
#which prints out the prediction of the one pixel with rgb of yellow. 

#real dataset would be filled with the a class but for example purposes I
#just used a pixel to represent each food.

im = Image.open("photos/mix.jpg")
pic = im.load()
x=im.width
y=im.height


colors = [0,0,0]
for i in range(0,y):
	for j in range(0,x):
		colors[0] += pic[i,j][0]
		colors[1] += pic[i,j][1]
		colors[2] += pic[i,j][2]

red = colors[0]/(x * y)
green = colors[1]/(x *y)
blue = colors[2]/(x * y)

#dataset is filled with 2 yellows and a black. yellow -> 1 black -> 2
dataset = [[255,255,0],[255,255,0],[0,0,0]]
target = [1,1,2]

#test would be the user's picture. in this case, its a scrambled egg
test = [[red,green,blue]]

#set up the log reg model under the var logreg. then fit the model with dataset
#and target
logreg = linear_model.LogisticRegression()
logreg.fit(dataset, target)

#prints the prediction using the logistic regression model.
result = logreg.predict(test)

