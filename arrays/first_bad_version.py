# Leetcode 278. First Bad Version

class Solution:
    def firstBadVersion(self, n):
        left,right=1,n
        while left<right:
            mid=(left+right)//2
            # isBadVersion is part of the leetcode api
            if not isBadVersion(mid):
                left=mid+1
            else:
                right=mid
        return left