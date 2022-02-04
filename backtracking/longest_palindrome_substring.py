class Solution:
    def longestPalindrome(self,s:str)->str:
        res=""
        res_len=0
        for i in range(len(s)):
            #odd length palindromes
            # i is the center position
            l,r=i,i
            while l>=0 and r<len(s) and s[l]==s[r]:
                if(r-l+1)>res_len:
                    res=s[l:r+1]
                    res_len=r-l+1
                l-=1
                r+=1
            #even length palindrome mean abccba
            l,r=i,i+1
            while l>=0 and r<len(s) and s[l]==s[r]:
                if(r-1+1)>res_len:
                    res=s[l:r+1]
                    res_len=r-l+1
                l-=1
                r+=1
        return res
    def brute(self,s:str)->str:
        max_len=0
        output=""
        for i in range(len(s)):
            for j in range(i+1,len(s)+1):
                candid=s[i:j]
                # reversing has n time. so total will be n^3
                if candid==candid[::-1] and len(candid)>max_len:
                    output=candid
                    max_len=len(candid)
        return output
s=Solution()
s.longestPalindrome("dkahfjkdshfjd")
print(s)

'''
For brute force solution, i go over each substring and check if it is palindrome. 
Checking if substring is palindrome it take n time complexiy. how many substrings we have
we have n^2 substring. total time complexity 
'''
# we have two aproaches to check if a string is palindrome:
# 1- we start from edges and compare the characters
# 2- we can start from at the middle and expand outwards
# we choose the 2. method. we are gonna take each char which is gonna be "n", to expand outwards it will be "n" again. 