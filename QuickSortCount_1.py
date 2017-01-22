#!/anaconda/bin/python
import itertools
def QuickSort(a):
	# Implement quick sort using the first element as the pivot always. This recursive
	# algorithm will also keep track of the number of comparisons made overall
	# First, partition the array using the first element as the pivot
	if len(a) <= 1:
		return a,0
	# Initialize the number of comparisons made to len(a)-1
	a,n = Partition(a,0,len(a)-1)
	return a,n
	
## Subroutines ##
def Partition(a,l,r):
	# Implementation of the partition subroutine used in the QuickSort function. The partition
	# subroutine is implemented as detailed below:
	# (1) Set a counter j = 0. This counter will keep track of the last seen element that is 
	#	  less than or equal to the pivot.
	# (2) Run a for loop over the 2nd to the final elements of the array, inclusive (note: the
	#	  pivot is always shifted so that it is the first element of the array).
	# (3) For each element, compare with the pivot. If it is less than the pivot, switch it with
	#	  the (j+1)st element and increment j. Else, do nothing.
	# (4) Place the pivot in its proper position
	# 
	# Initialize a j counter
	if r-l == 1:
		if a[r] < a[l]:
			a_temp = a[r]
			a[r] = a[l]
			a[l] = a_temp
		return a,1
	if r-l <= 0:
		return a,0
	j = l+1
	# Run the for loop
	for i in itertools.count(l+1):
		if i < r+1:
			# Compare the next element in the array to the pivot
			if a[i] < a[l]:
				# Switch the elements in position j (after increment) and i
				a_temp = a[j]
				a[j] = a[i]
				a[i] = a_temp
				# Increment j
				j = j + 1
		else:
			break
	# Now, put the pivot in its proper position.
	a_temp = a[l]
	a[l] = a[j-1]
	a[j-1] = a_temp
	n = r-l
	# Partitition the lower part of the matrix
	a,n_l = Partition(a,l,j-2)
	

	# Partition the upper part of the matrix
	a,n_u = Partition(a,j,r)

	return a,n+n_u+n_l

