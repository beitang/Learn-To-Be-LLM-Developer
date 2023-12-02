class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        commonPrefix = ""
        if len(strs) == 1:
            return strs[0]
        for i in range(len(strs[0])):
            for j in range(1, len(strs)):
                if len(strs[j]) < i + 1 or strs[0][i] != strs[j][i]:
                    return commonPrefix
                if j == len(strs) - 1:
                    commonPrefix += strs[0][i]
        return commonPrefix
