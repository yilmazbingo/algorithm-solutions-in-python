'''
You are given an array people where people[i] is the weight of the ith person, and an infinite number of boats where each boat can carry a maximum weight of limit.
Each boat carries at most two people at the same time, provided the sum of the weight of those people is at most limit.

Return the minimum number of boats to carry every given person.
'''

class Solution(object):
    def numRescueBoats(self, people, limit):
        # list.sort() modifies the list.
        #  list sort() has been using the Timsort algorithm since version 2.3. This algorithm has a runtime complexity of O(n. logn).
        people.sort()
        i,j=0, len(people)-1
        boats=0
        while i<=j:
            if people[j]+people[i]<=limit:
                boats+=1
                j-=1
                i+=1
            else:
                # if not just send one person with heavier
                j-=1
                boats+=1
        return boats