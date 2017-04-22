import math
from decimal import Decimal

def readFromText():
	points = []
	f = open("input.txt")
	next = f.readline()
	while next != "":
		num1 = Decimal(next.split()[0])
		num2 = Decimal(next.split()[1])
		tuplePoint = (num1, num2)
		points.append(tuplePoint);
		next = f.readline()
	return points

def distanceFormula(x, y):
	return math.sqrt((x[0] - y[0])**2 + (x[1] - y[1])**2)

def bruteForce(arr):
	min = distanceFormula(arr[0], arr[1])
	for i in range(0, len(arr)):
		for j in range(i + 1 ,len(arr)):
			dist = distanceFormula(arr[i], arr[j])
			if dist < min:
				min = dist;
	return min

arr = readFromText()
distance = bruteForce(arr)
text_file = open("input_distance.txt", "w")
text_file.write(str(distance))
text_file.close()
