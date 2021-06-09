'''
You may recall that an array A is a mountain array if and only if:

A.length >= 3
There exists some i with 0 < i < A.length - 1 such that:
A[0] < A[1] < ... A[i-1] < A[i]
A[i] > A[i+1] > ... > A[A.length - 1]
Given a mountain array mountainArr, return the minimum index such that mountainArr.get(index) == target.  If such an index doesn't exist, return -1.

You can't access the mountain array directly.  You may only access the array using a MountainArray interface:

MountainArray.get(k) returns the element of the array at index k (0-indexed).
MountainArray.length() returns the length of the array.
Submissions making more than 100 calls to MountainArray.get will be judged Wrong Answer.  Also, any solutions that attempt to circumvent the judge will result in disqualification.
'''

class Solution:
    def findInMountainArray(self, target: int, mountain_arr: 'MountainArray') -> int:
        l = 0
        r = mountain_arr.length() - 1
        while(l <= r):
            m = l + (r-l)//2
            mid = mountain_arr.get(m)
            if mid < mountain_arr.get(m + 1):
                l = m + 1
            elif mountain_arr.get(m - 1) > mid:
                r = m - 1
            else:
                if mid == target:
                    return m
                elif mid < target:
                    return -1
                else:
                    l, r = 0, m - 1
                    while(l <= r):
                        m = l + (r - l)//2
                        mid = mountain_arr.get(m)
                        if mid == target:
                            return m
                        elif mid > target:
                            r = m - 1
                        else:
                            l = m + 1
                    l, r = m + 1, mountain_arr.length() - 1
                    while(l <= r):
                        m = l + (r - l)//2
                        mid = mountain_arr.get(m)
                        if mid == target:
                            return m
                        elif mid > target:
                            l = m + 1
                        else:
                            r = m - 1
                return -1