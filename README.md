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
