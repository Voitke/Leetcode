class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        return self.addOneToDigit(digits, len(digits) - 1)

    # recursion
    def addOneToDigit(self, digits, index):
        if digits[index] != 9:
            digits[index] = digits[index] + 1
        elif index == 0 and digits[index] == 9:
            digits[index] = 0
            digits.insert(0, 1)
        else:
            digits[index] = 0
            return self.addOneToDigit(digits, index - 1)
        return digits