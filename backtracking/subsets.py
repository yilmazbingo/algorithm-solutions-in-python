# Given a set of distinct integers, nums, return all possible subsets
# Set must not contain duplicate subsets

def subsets(nums):
    ans=[]
    current=[]
    # this is the backtracking method
    solution(nums,ans,current,0)
    return ans

# we use index to see if we exhausted the list
def solution(nums,ans,current,index):
    # this is the base case to exit the recursion
    if index>len(nums):
        return
    # initially [[]] empty set will be appended
    ans.append(current[:])
    for i in range(index,len(nums)):
        if nums[i] not in current:
            # We ask should we take it
            current.append(nums[i])
            solution(nums,ans,current,i)
            # we pop it after we process it
            current.pop()
    return