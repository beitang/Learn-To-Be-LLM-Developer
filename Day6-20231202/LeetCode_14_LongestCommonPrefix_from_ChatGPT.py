class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs:  # 检查空列表
            return ""

        # 如果只有一个字符串，直接返回该字符串
        if len(strs) == 1:
            return strs[0]

        commonPrefix = ""
        shortest_str_length = min(len(s) for s in strs)  # 找到最短字符串的长度

        for i in range(shortest_str_length):
            current_char = strs[0][i]

            if all(s[i] == current_char for s in strs):
                commonPrefix += current_char
            else:
                break

        return commonPrefix
