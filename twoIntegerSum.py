class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        count = {}

        for index, val in enumerate(nums):
            inverse = target - val

            if inverse in count:
                return [count[inverse], index]
            count[val] = index
