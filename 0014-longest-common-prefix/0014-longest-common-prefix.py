class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        min_length = 200
        for i in range(len(strs)):
            min_length = min (min_length, len(strs[i]))

        count = 0   
        output = "" 
        for i in range(min_length):
            count = 0
            for j in range(len(strs)):
                if strs[j][i] == strs[0][i]:
                    count += 1
                if count == len(strs):
                    output += strs[0][i]
            
        return output

        