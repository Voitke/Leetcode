class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        alreadySeen = []
        for index in range(len(nums)):
            if nums[index] not in alreadySeen:
                alreadySeen.append(nums[index])
            else:
                nums[index] = None

        index = 0
        while index < len(nums):
            if nums[index] == None:
                nums.pop(index)
                index -= 1
            index += 1

        return len(nums)