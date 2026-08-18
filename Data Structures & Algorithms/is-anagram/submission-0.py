class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # if the strings are different lengths they cannot be anagrams
        if len(s) != len(t):
            return False
        # create a hashmap using the letters as keys and occurrence as values
        recurringLetters = {}
        for ch in s:
            if ch in recurringLetters:
                recurringLetters[ch] += 1
            else:
                recurringLetters[ch] = 1
        
        # there is surely a more space complexity effective way to handle this but i'm blanking out
        recurringLettersSecond = {}
        for ch in t:
            if ch in recurringLettersSecond:
                recurringLettersSecond[ch] += 1
            else:
                recurringLettersSecond[ch] = 1
        return recurringLetters == recurringLettersSecond

        # an alternative approach would be to sort both strings and check if they are equal (oops!)

        