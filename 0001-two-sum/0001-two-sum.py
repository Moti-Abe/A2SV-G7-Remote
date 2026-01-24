class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        my_dict = {}
        for i in range(len(nums)):
            my_dict[nums[i]] = i
        for i in range(len(nums)):
            comp = target - nums[i]
            if comp in nums and my_dict[comp] != i:
                return [my_dict[comp],i]