class Solution:
    def isValid(self, s: str) -> bool:
        closingBrackets = {
            "{": "}", 
            "(": ")",
            "[": "]"
        }
        queue = []
        isValid = False
        for index in range(len(s)):
            if s[index] in closingBrackets.keys():
                queue.append(s[index])
            elif queue and s[index] == closingBrackets[queue.pop(len(queue) - 1)]:
                isValid = True
            else:
                isValid = False
                break
        return isValid and not queue