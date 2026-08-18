class Solution:
    def isPalindrome(self, s: str) -> bool:
        acceptableLetters = "abcdefghijklmnopqrstuvwxyz0123456789"
        fixedStr = [ch.lower() for ch in s if ch.lower() in acceptableLetters]
        start = 0
        end = len(fixedStr) - 1
        # O(logn)
        while (start < end):
            # if s[start].lower() not in acceptableLetters:
            #     start += 1
            # if s[end].lower() not in acceptableLetters:
            #     end -= 1

            if fixedStr[start] != fixedStr[end]:
                return False
            start += 1
            end -= 1
        return True