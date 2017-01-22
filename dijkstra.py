from heapq import *
def dijkstra(g):
	# Implement dijkstra's shortest path algorithm for the graph g.
	# The algorithm implementation is detailed below:
	#
	# (1) Initialize X = [] to store the vertices already processed
	# (2) Initilize A = {v: 0 for v in g} to store the shortest path to each vertex in the
	#	  graph. 
	# (3) Let V = the set of vertices in g. Run the while loop below:
	#	  while V != X:
	#	   (a) Look at edges crossing X to V-X. Compute their distance.
	#	   (b) Add the edge w to X that minimizes A[v]+l_{vw}, where v is the
	#		   vertex in X which points to w while minimizing the above quantity,
	#	   (c) Set A[w] = A[v] + l_{vw}
	#
	# In order to make this algorithm run efficiently, we will use a heap to store
	# the components of the graph which cross the horizon between searched and unsearched nodes

	# Initialize X, the list storing the vertices already processed
	X = []
	# Initialize A, the dict storing the distance from the source to each vertex
	A = {k: float('inf') for k in g}
	A[1] = 0
	# Now, initilize the heap to store the lengths of the edges crossing V-X. Note that
	# in python this is done by simply initializing an empty list and adding elements
	# with the heappush operation
	h = [(float('inf'),k) for k in g]
	del h[0]
	# Now, add the first vertex to X
	X.append(1)
	# Now, update the heap so that the length of the edges that node 1 points to are given
	# by the length of 1 to the node
	for w,v in g[1]:
		for i,p in enumerate(h):
			p,n = p
			if n == v:
				if w < p:
					del h[i]
					heappush(h,(w,v))
					break
	# Now, run the main loop
	while len(h) > 0:
		# Pop the heap to get the smallest Dijkstra greedy score
		heapify(h)
		d,v = heappop(h)
		# Now, add v to X
		X.append(v)
		# Update the Dijkstra greedy score for v
		A[v] = d
		# Now, update the Dijkstra greedy score for the nodes attached to w
		for d,w in g[v]:
			for i,p in enumerate(h):
				p,n = p
				if n == w:
					if d + A[v] < p:
						h[i]= (d+A[v],w)
	print X
	print len(X)
	return A