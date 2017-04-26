import math
from decimal import Decimal

#reads from input file and stores tuple points in array
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

 #intex = 1 for sorted y, 0 for sorted x in tuple

 #sorts array of tuples in x or y value
 #intex = 1 for sorted y, 0 for sorted x in tuple
 
def mergeSort(alist, index):
    if len(alist)>1:
        mid = len(alist)//2
        lefthalf = alist[:mid]
        righthalf = alist[mid:]

        mergeSort(lefthalf, index)
        mergeSort(righthalf, index)

        i=0
        j=0
        k=0
        while i < len(lefthalf) and j < len(righthalf):
            if lefthalf[i][index] < righthalf[j][index]:
                alist[k]=lefthalf[i]
                i=i+1
            else:
                alist[k]=righthalf[j]
                j=j+1
            k=k+1

        while i < len(lefthalf):
            alist[k]=lefthalf[i]
            i=i+1
            k=k+1

        while j < len(righthalf):
            alist[k]=righthalf[j]
            j=j+1
            k=k+1

def divide_and_conquer(arr): 
	if len(arr) == 1:
		return float('inf')
	if len(arr) == 2:
		return distanceFormula(arr[0], arr[1])

	#splits into left and right subdivisions and sets min value to d
	mid = len(arr)//2
	lefthalf = arr[:mid]
	righthalf = arr[mid:]
	d = min(divide_and_conquer(lefthalf), divide_and_conquer(righthalf))

	#checks if there is min value over the division line
	newArr = [x for x in arr if x[0] >= mid - d and x[0] <= mid + d]
	mergeSort(newArr, 1)
	return min(bruteForce(newArr), d)

arr = readFromText()

# distance = bruteForce(arr)
distance = divide_and_conquer(arr)

text_file = open("input_distance.txt", "w")
text_file.write(str(distance))
text_file.close()
