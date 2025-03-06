class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for index1 in range(len(nums)):
            for index2 in range(len(nums)):
                if index1 == index2:
                    continue
                if nums[index1] + nums[index2] == target:
                    return [index1, index2]
