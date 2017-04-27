import math
import sys
from decimal import Decimal
import time


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
	min = float('inf')
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

def dc(arr):
	#overall smallest distance (faster than best distance on recursive call)
	best = [distanceFormula(arr[0], arr[1])]
	def divide_and_conquer(arr): 
		if len(arr) == 1:
			return arr
		if len(arr) == 2:
			return sorted(arr, key=lambda x: x[0])

		#splits into left and right subdivisions
		mid = len(arr)//2
		midx = arr[mid][0]
		arr = list(mergeY(divide_and_conquer(arr[:mid]), divide_and_conquer(arr[mid:])))

		#removes points that are > d from the division line, this new arr is newArr
		#then for each point in newArr checks 7 other points or until end of the newArr.
		newArr = [x for x in arr if abs(x[0]-midx) < best[0]]
		for i in range(len(newArr)):
			for j in range(1,8):
				if i+j < len(newArr):
					best[0] = min(distanceFormula(newArr[i],newArr[i+j]),best[0])

		return arr 
	arr.sort()
	divide_and_conquer(arr)
	return best[0]

start_time = time.time()
arr = readFromText()
#checks if correct agruments
if arr != -1:
	#distance = bruteForce(arr)
	
	distance = dc(arr)

	#distance = distanceFormula(closestpair(arr)[0], closestpair(arr)[1])
	
	print("--- %s seconds ---" % (time.time() - start_time))

	#get argument 1 name.
	if sys.argv[1].endswith('.txt'):
		file_name = sys.argv[1][:-4]

	text_file = open(file_name + "_distance.txt", "w")
	text_file.write(str(distance))
	text_file.close()