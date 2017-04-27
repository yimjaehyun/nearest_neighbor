import math
import sys
from decimal import Decimal

#reads from input file and stores tuple points in array
def readFromText():
	#handles no arguments
	try:
        	arg1 = sys.argv[1]
    	except IndexError:
	        print "Error: Too few little argument."
	        sys.exit(1)
	points = []
	f = open(sys.argv[1])
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

#sorts array A and B if size = 2 and merges then in order of Y.
def mergeY(A,B):
	if len(A) == 2:
		if A[1][1] > A[0][1]:
			A[0], A[1] = A[1], A[0]
	if len(B) == 2:
		if B[1][1] > B[0][1]:
			B[0], B[1] = B[1], B[0]
	return sorted((A+B),key=lambda x:(x[1]))

def divide_and_conquer(arr): 
	if len(arr) == 1:
		return float('inf'), arr
	if len(arr) == 2:
		return distanceFormula(arr[0], arr[1]), arr

	#splits into left and right subdivisions and sets min value to d
	# arr = 
	mid = len(arr)//2
	dL, arrL = divide_and_conquer(arr[:mid])
	dR, arrR = divide_and_conquer(arr[mid:])
	arr = mergeY(arrL, arrR)
	d = min(dL, dR)

	#removes points that are > d from the division line, this new arr is newArr
	#then for each point in newArr checks 7 other points or until end of the newArr.
	newArr = [x for x in arr if x[0] >= mid - d and x[0] <= mid + d]
	for i in range(0, len(newArr)):
		count = 0
		for j in range(i + 1 ,len(newArr)):
			d = min(distanceFormula(newArr[i],newArr[j]),d)
			if count == 7:
				j = len(newArr)
				break
	return d, arr #returns tuple of d and arr

arr = readFromText()
#checks if correct agruments
if arr != -1:
	# distance = bruteForce(arr)
	distance = divide_and_conquer(arr)[0]
	arr2 = divide_and_conquer(arr)[1]

	#get argument 1 name.
	if sys.argv[1].endswith('.txt'):
		file_name = sys.argv[1][:-4]

	text_file = open(file_name + "_distance.txt", "w")
	text_file.write(str(distance))
	text_file.close()