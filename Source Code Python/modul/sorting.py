def bubblesort(alist):
	for i in range(0, len(alist)-1):
		for j in range(len(alist)-1, i, -1):
			if alist[j] < alist[j-1]:
				temp = alist[j]
				alist[j] = alist[j-1]
				alist[j-1] = temp

def selectionsort(alist):
	for i in range(0, len(alist)-1):
		minposition = len(alist)-1
		for j in range(len(alist)-2, i-1, -1):
			if alist[j] < alist[minposition]:
				minposition = j
		temp = alist[i]
		alist[i] = alist[minposition]
		alist[minposition] = temp

def insertionsort(alist):
	for i in range(1, len(alist)):
		currentvalue = alist[i]
		position = i
		while position > 0 and alist[position-1] > currentvalue:
			alist[position] = alist[position-1]
			position -= 1
		alist[position] = currentvalue

def shellsort(alist):
	# fungsi lokal
	def insort(alist, start, step):
		for i in range(start+step, len(alist), step):
			currentvalue = alist[i]
			position = i
			while position >= step and \
				  alist[position-step] > currentvalue:
				alist[position] = alist[position-step]
				position -= step
			alist[position] = currentvalue
	# shell sort
	step = len(alist) // 2
	while step > 0:
		for i in range(step):
			# memanggil fungsi insort()
			insort(alist, i, step)
		step = step // 2
