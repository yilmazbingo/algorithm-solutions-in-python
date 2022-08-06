'''
278.Easy First Bad Version

You are a product manager and currently leading a team to develop a new product. Unfortunately, the latest version of your product fails the quality check.
Since each version is developed based on the previous version, all the versions after a bad version are also bad.

Suppose you have n versions [1, 2, ..., n] and you want to find out the first bad one, which causes all the following ones to be bad.

You are given an API bool isBadVersion(version) which returns whether version is bad. Implement a function to find the first bad version. You should minimize the number of calls to the API.
'''

class Solution:
    def firstBadVersion(self, n):
        # left and right are versions
        left,right=1,n
        while left<right:
            mid=(left+right)//2
            # isBadVersion is part of the leetcode api
            if not isBadVersion(mid):
                # if it is not bad, we do not include mid
                left=mid+1
            else:
                # if it is bad we include mid
                right=mid
        return left # or right