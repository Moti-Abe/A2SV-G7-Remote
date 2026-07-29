class Solution:
    def minimumSum(self, num: int) -> int:
        string_num = str(num)
        s = list(string_num)
        for i in range(4):
            s[i] = int(s[i])
        s.sort()
        new1 = ""+str(s[0])+str(s[2])
        
        new2 = ""+str(s[1])+str(s[3])
        
        return (int(new1)+int(new2))
        
# ✅ Correct solution. Time complexity: O(1) (fixed 4 digits), Space: O(1)
# Optimal approach achieved. The sorted digits are combined as [smallest + middle] and [middle + largest] to minimize sum.

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna