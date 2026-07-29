class Solution:
    def transformArray(self, nums: List[int]) -> List[int]:
        for i in range(len(nums)):
            if nums[i]%2 == 0:
                nums[i] = 0
            else:
                nums[i] = 1
        
        nums.sort()
        
        return nums
            

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna