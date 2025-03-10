class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        prefix = ""
        letterIndex = 0
        while True:
            try:
                candidate = strs[0][letterIndex]
                for wordIndex in range(1, len(strs)):
                    if strs[wordIndex][letterIndex] != candidate:
                        candidate = ""
                        break
                if candidate == "":
                    break
                prefix += candidate
                letterIndex += 1
            except IndexError:
                break
        return prefix