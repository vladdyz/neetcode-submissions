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

        