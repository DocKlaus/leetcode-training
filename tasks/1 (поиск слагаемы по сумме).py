class Solution(object):
    def twoSum(self, nums: list[int], target: int) -> list:
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        answers = {}
        for i, num in enumerate(nums):
            answer = target - num
            if answer in answers:
                return [answers[answer], i]
            answers[num] = i


nums = [2, 7, 11, 15]
target = 9

sol = Solution()
print(sol.twoSum(nums, target))
