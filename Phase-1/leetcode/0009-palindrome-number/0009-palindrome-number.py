class Solution:
    def isPalindrome(self, x: int) -> bool:
        s = str(x)
        rev_str = s[::-1]
        if s == rev_str:
            return True
        else:
            return False

        
        