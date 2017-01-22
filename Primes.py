from itertools import *

def erato_sieve(N):
    if N < 2:
        return []
    else:
        nums = range(2,N+1,1)
        for ii,v in enumerate(nums):
            for jj in range(len(nums)-1,ii+1,-1):
                if nums[jj] % v == 0:
                    del nums[jj]
        return nums

def main():
    print erato_sieve(10000)

if __name__ == '__main__':
    main()