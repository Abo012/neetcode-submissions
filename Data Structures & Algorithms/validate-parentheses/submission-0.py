
class Solution:
    def isValid(self, s: str) -> bool:
        stack = []

        closeToOpen = {
            ")": "(",
            "]": "[",
            "}": "{"
        }

        for c in s:

            # If current character is a closing bracket
            if c in closeToOpen:

                # Check whether stack is not empty
                # and the top matches the expected bracket
                if stack and stack[-1] == closeToOpen[c]:
                    stack.pop()
                else:
                    return False

            # Otherwise, push opening bracket
            else:
                stack.append(c)

        # All opening brackets must be matched
        return len(stack) == 0
