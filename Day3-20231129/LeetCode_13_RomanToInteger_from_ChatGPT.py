class Solution:
    def romanToInt(self, s: str) -> int:
        roman_to_integer = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
        int_value = 0
        n = len(s)

        for i in range(n):
            # 如果不是最后一个字符且当前字符代表的值小于下一个字符的值，则减去当前字符的值
            if i < n - 1 and roman_to_integer[s[i]] < roman_to_integer[s[i + 1]]:
                int_value -= roman_to_integer[s[i]]
            else:
                # 否则加上当前字符的值
                int_value += roman_to_integer[s[i]]

        return int_value
