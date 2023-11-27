class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        num_map = {}  # 创建一个空字典用来存储数字及其索引
        for i, num in enumerate(nums):
            complement = target - num
            if complement in num_map:
                return [num_map[complement], i]  # 如果找到了配对，返回其索引
            num_map[num] = i  # 将当前数字及其索引存入字典

