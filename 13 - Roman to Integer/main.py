class Solution:
    def romanToInt(self, s: str) -> int:
        values = {
            "I": 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000
        }
        integer = 0
        for indexOfNumeral in range(len(s)):
            integer += values[s[indexOfNumeral]]
            if(indexOfNumeral > 0 and values[s[indexOfNumeral-1]] < values[s[indexOfNumeral]]):
                integer -= 2 * values[s[indexOfNumeral-1]]
        return integer