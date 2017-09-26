import csv
import random

def getOccupations():
	occupations = {}

	with open("data/occupations.csv", "r") as file:
		reader = csv.reader(file)
			
		#toss out the first row
		reader.next()
		
		for x in reader:
			occupations[x[0]] = float(x[1])
			
		return occupations

def sign(x, y):
	if x > y:
		return 1
	return -1


def getRandomOccupation(occupations):
	percents = []
	total = 0.0

	for elem in occupations:
		if elem == "Total":
			total = float(occupations[elem])
		else:
			percents.append([float(occupations[elem]), elem])

	for x in range(0, len(percents)):
		percents[x][0] /= total

	#the idea is to get a cumulative count
	percents.sort(sign)

	for x in range(0, len(percents) - 1):
		percents[x+1][0] += percents[x][0]

	rand = random.random()

	for x in percents:
		if rand <= x[0]:
			return x[1]

