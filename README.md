# Algorithms

Repository of basic algorithms that I've studied and written code for. 

Files:
- Primes.py (01-21-2017): Implementation of the Erato Sieve.
Includes a function to return a list enumerating all primes less than or equal to an integer N.
Possible Updates:
(1) Type Checking Inputs
(2) Memoization of known primes for faster computation and dynamically resizing the primes list
- QuickSortCount.py (01-21-2017): Implementation of the QuickSort algorithm, with a counter for the number of 
comparisons made. This algorithm always uses the first element of an array as the pivot, and is thus not necessarily 
optimized. 
Possible Updates:
(1) The recursion is implemented a bit sloppily. I don't have time to fix this right now, but most of the work is done by the
Partition function, which is supposed to be a helper function. Ideally, the recursive portion would be shifted onto the 
QuickSort function
(2) Randomized pivots with an appropriate RNG to optimize the algorithm.

-Djikstra.py (01-21-2017): Implementation of Djikstra's algorithm for finding the shortest path between two nodes in a graph.
Note that this implementation makes use of a heap, but likely not in the most efficient way. 
Possible Updates:
(1) Instead of using python's built in heap class, program an augmented heap in which a dictionary indexed by the nodes in the
heap points to the index of each node in the actual heap. Upon adding new elements to the heap, the dictionary will also be
updated.
