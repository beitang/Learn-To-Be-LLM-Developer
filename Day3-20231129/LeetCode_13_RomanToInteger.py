roman_to_integer = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}

class Solution:
    def romanToInt(self, s: str) -> int:
        int_value = 0
        for i in range(len(s)):
            if i < len(s) - 1:
                if s[i] == "I" and (s[i + 1] == "V" or s[i + 1] == "X"):
                    int_value -= 1
                elif s[i] == "X" and (s[i + 1] == "L" or s[i + 1] == "C"):
                    int_value -= 10
                elif s[i] == "C" and (s[i + 1] == "D" or s[i + 1] == "M"):
                    int_value -= 100
                else:
                    int_value += roman_to_integer[s[i]]
            else:
                int_value += roman_to_integer[s[i]]
        return int_value
