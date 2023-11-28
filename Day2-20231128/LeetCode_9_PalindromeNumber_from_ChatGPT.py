class Solution:
    def isPalindrome(self, x: int) -> bool:
        # 负数和尾数为0但不是0本身的数字不是回文数
        if x < 0 or (x % 10 == 0 and x != 0):
            return False

        reversed_number = 0
        while x > reversed_number:
            reversed_number = reversed_number * 10 + x % 10
            x = x // 10

        # 对于偶数位数字，x 和 reversed_number 应相等；
        # 对于奇数位数字，应忽略 reversed_number 的最后一位。
        return x == reversed_number or x == reversed_number // 10

