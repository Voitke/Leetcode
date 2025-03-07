class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0: 
            return False
        else:
            pictographicForm = str(x)
            digitLength = len(pictographicForm)
            for i in range(0, digitLength // 2):
                if pictographicForm[i] != pictographicForm[digitLength - 1 - i]:
                    return False
            return True