class Solution:
    def numberGame(self, nums: List[int]) -> List[int]:
        nums.sort()
        for i in range (0,len(nums)-1,2):
            temp = nums[i]
            nums[i] = nums[i+1]
            nums[i+1] = temp
            
        return nums


# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna