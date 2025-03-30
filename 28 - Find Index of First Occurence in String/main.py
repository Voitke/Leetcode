class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        index = -1
        for i in range(len(haystack)):
            if haystack[i] == needle[0] and haystack[i:i+len(needle)] == needle:
                index = i
                break
        return index