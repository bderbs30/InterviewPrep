class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        count = {}

        for i in range(len(nums)):
            count[nums[i]] = i

        for index, val in enumerate(count):
            inverse = target - val
            if inverse in count and count[inverse] != index:
                return sorted([index, count[target - val]])
