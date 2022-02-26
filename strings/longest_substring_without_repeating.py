'''
3. Medium Longest Substring Without Repeating Characters

Given a string s, find the length of the longest substring without repeating characters.
'''


class Solution:
    # brute force with two pointer technique
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) < 2:
            return len(s)
        longest = 0
        for i in range(len(s)):
            seen = {}
            current_length = 0
            for j in range(i, len(s)):
                current_char = s[j]
                if current_char not in seen:
                    seen[current_char] = True
                    current_length += 1
                    longest = max(current_length, longest)
                else:
                    break
        return longest
    # Sliding window, form a window over some portion of sequential data, then move that window throughout the data to capture different parts.
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s)<2:
            return len(s)
        seen=set()
        l=0
        longest=0
        for r in range(len(s)):
            # we are shrinking our window after we remove the seen value
            while s[r] in seen:
                seen.remove(s[l])
                l+=1
            seen.add(s[r])
            longest=max(longest,r-l+1)
        return longest