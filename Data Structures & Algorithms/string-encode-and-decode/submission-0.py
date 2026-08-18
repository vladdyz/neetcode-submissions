class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded = ""
        return encoded.join(string + "wowcool" for string in strs)

    def decode(self, s: str) -> List[str]:
        strings = s.split("wowcool")
        strings.pop() # The last index will always hold "" because of the string math in encode
        return strings