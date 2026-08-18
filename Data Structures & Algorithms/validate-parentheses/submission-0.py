class Solution:
    def isValid(self, s: str) -> bool:
        # I am dumb this should use a stack
        stack = []
        for ch in s:
            if ch in "])}":
                # safety in case the first character is a closing bracket
                if stack:
                    closing = stack.pop()
                else:
                    return False
                match ch:
                    case "]":
                        if closing != "[":
                            return False
                    case ")":
                        if closing != "(":
                            return False
                    case "}":
                        if closing != "{":
                            return False
            else:
                # All characters are either "{}[]()", don't need to filter out alphanum
                stack.append(ch)
        if stack:
            return False
        return True


        