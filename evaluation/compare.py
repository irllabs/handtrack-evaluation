#Evaluation script for hand segmentation and tracking algorithms

#Script evaluates performace of a hand segmentation and tracking
#algorithm, against a ground truth

#To run in command line:
#python compare.py <path to ground truth> <path to algorithm>

#Paths should be to text files containing fingertip positions of hand
#in each line. The fingers should be ordered from highest to lowest.

import sys, math

def compare(path1, path2):
	#path1 - ground truth
	#path2 - algorithm to compare

	fOpen = open(path1, 'r')
	#Parse the points into entries
	table1 = [line.strip().split(',') for line in fOpen.readlines()]

	fOpen = open(path2, 'r')
	#Parse the points into entries
	table2 = [line.strip().split(',') for line in fOpen.readlines()]

	n = len(table1)
	skipFrames = n/10
	table1 = table1[skipFrames:-skipFrames]
	table2 = table2[skipFrames:-skipFrames]

	#Make table2 have more entries (fps)
	if len(table1) > len(table2):
		temp = table2
		table2 = table1
		table1 = temp

	n = len(table1)
	m = len(table2)
	table1 = table1[:-(n%5)]
	table2 = table2[:-(m%5)]
	n = len(table1)/5
	m = len(table2)/5

	ratio = m/n

	error = 0.0

	for i in xrange(n):
		start = i*5
		end = (i+1)*5
		vals1 = table1[start:end]
		if ratio > 1:
			start = (ratio-1)*i*5
			end = (ratio-1)*(i+1)*5
		vals2 = table2[start:end]

		lError = 0.0

		for j in xrange(5):
			x1 = float(vals1[j][0])
			y1 = float(vals1[j][1])
			x2 = float(vals2[j][0])
			y2 = float(vals2[j][1])

			lError += math.pow(x2 - x1, 2) + math.pow(y2 - y1, 2)

		error += math.sqrt(lError)

	print 'The Mean Squared Error is: ' + str(error/m)

	return

def main():
	compare(sys.argv[1], sys.argv[2])

if __name__ == '__main__':
	main()
