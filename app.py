from flask import Flask, render_template
import csv
import random

app = Flask(__name__)





occupations = {}

percents = []

total = 0.0

with open("occupations.csv", "r") as file:
	reader = csv.reader(file)
	
	#toss out the first row
	reader.next()
	
	for x in reader:
		occupations[x[0]] = float(x[1])
		
		if x[0] != "Total":
			percents.append([float(x[1]), x[0]])
		else:
			total = float(x[1])



#scale by 99.8
for x in range(0, len(percents)):
	percents[x][0] /= total

def sign(x, y):
	if x > y:
		return 1
	return -1

#the idea is to get a cumulative count
percents.sort(sign)

for x in range(0, len(percents) - 1):
	percents[x+1][0] += percents[x][0]

def getOccupation():
	rand = random.random()

	for x in percents:
		if rand <= x[0]:
			return x


@app.route('/occupations')
def occupations():
	u = []
	u.append({"name":"test", "percent":6.7})
	return render_template('index', occupations=u)

if __name__ == "__main__":
	app.debug = True
	app.run()
