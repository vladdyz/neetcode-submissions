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
        # - Both loops need to work with the leading pointer (j) instead of my implementation (where the outer loop increments the trailing pointer and the inner loop looks ahead with the leading pointer)
        # I spent way too long stubbornly trying to optimize the performance of my initial solution
        longest = 0
        charSet = set()
        i = 0  # The trailing pointer (left side of window)
        
        # increment the lookahead (j) instead of the trail (i) each iteration
        for j in range(len(s)):  
            
            # if the leading pointer hits a duplicate character, remove one character at a time from the
            # left side of the string until the duplicate character has been removed
            # ex: abfcgbfg -> when j reaches the 2nd f, remove 'a' then 'b' then 'f'.
            while s[j] in charSet:
                charSet.remove(s[i])
                i += 1 
                
            # continue from where j was
            charSet.add(s[j])
            
            # more elegant than writing a conditional statement (if j-i+1 > longest...)
            longest = max(longest, j - i + 1)
                
        return longest



        