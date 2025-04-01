class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        count = 0
        trailingSpacesTraversed = False
        for character in reversed(s):
            if character != " ":
                trailingSpacesTraversed = True
                count = count + 1
            elif character == " " and trailingSpacesTraversed:
                break
        return count