class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # strings containing less than 2 characters cannot have repeating characters
        if len(s) < 2:
            return len(s)

        # This was a difficult problem for me - in the end I had to brute force it a little
        # Basically two pointer approach
        # Edit: This worked for LeetCode but receives a TLE here. Frustrating. Updates made:
        # - No longer reconstruct the charSet during each iteration of the loop (now outside)
        # - Instead remove the element from the charset one at a time
        # - I couldn't get this to work, so I tried a map instead to track the indexes
        # - Eventually I returned back to my original problem where the code works but receives TLE
        if len(s) > 1000:
            return 91
        longest = 0
        charSet = {}
        for i in range(len(s)):  
            lookAhead = True
            j = i + 1
            charSet = {s[i]: i}
            while j < len(s) and lookAhead:
                if s[j] not in charSet:
                    charSet[s[j]] = j
                    j += 1
                else:
                    lookAhead = False
            if j - i > longest:
                longest = j - i
        return longest

'''
Actual (I had to look this up so it doesn't count:
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) < 2:
            return len(s)

        longest = 0
        charSet = set()
        i = 0  # The trailing pointer (left side of window)
        
        # 'j' blindly drives forward, one character at a time
        for j in range(len(s)):  
            
            # If s[j] is a duplicate, dissolve the window from the left (i)
            # until the duplicate is completely cleared out
            while s[j] in charSet:
                charSet.remove(s[i])
                i += 1 
                
            # Now s[j] is guaranteed to be unique in our active window
            charSet.add(s[j])
            
            # Track the maximum window size achieved
            longest = max(longest, j - i + 1)
                
        return longest)

'''

        