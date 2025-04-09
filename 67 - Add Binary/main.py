class Solution:
    def addBinary(self, a: str, b: str) -> str:
        a = ('0' * (len(b) - len(a))) + a
        b = ('0' * (len(a) - len(b))) + b
 
        a = [int(bit) for bit in a]
        b = [int(bit) for bit in b]
 
        index = len(a) - 1
        result = []
        carryBit = 0

        while index != -1:
            tmpBit = a[index] + b[index] + carryBit
            match tmpBit:
                case 0: result.append(0)
                case 1:
                    result.append(1)
                    carryBit = 0
                case 2:
                    result.append(0)
                    carryBit = 1
                case 3:
                    result.append(1)
            index = index - 1
        if carryBit == 1:
            result.append(1)
        result.reverse()

        return "".join(map(str, result))