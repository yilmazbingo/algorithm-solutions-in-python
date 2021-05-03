# Given a set of distinct integers, nums, return all possible subsets
# Set must not contain duplicate subsets

def subsets(nums):
    ans=[]
    current=[]
    solution(nums,ans,current,0)
    return ans

def solution(nums,ans,current,index):
    # this is the base case to exit the recursion
    if index>len(nums):
        return
    # initially [[]] empty set will be appended
    ans.append(current[:])
    for i in range(index,len(nums)):
        if nums[i] not in current:
            current.append(nums[i])
            solution(nums,ans,current,i)
            current.pop()
    return