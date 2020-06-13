"""
Given a set of distinct positive integers, find the largest subset such that every pair (Si, Sj) of elements in this subset satisfies:

Si % Sj = 0 or Sj % Si = 0.

If there are multiple solutions, return any subset is fine.

Example 1:
Input: [1,2,3]
Output: [1,2] (of course, [1,3] will also be ok)
"""


def largestDivisibleSubset(nums):
    """
    :param nums: [integers]
    :return: [integers]
    """
    # sort nums to insure that all of the numbers that divides nums[i] preceeds it
    nums.sort()
    res = [[num] for num in nums]
    for i in range(len(nums)):
        for j in range(i):
            if nums[i] % nums[j] == 0 and len(res[i]) < len(res[j]) + 1:
                res[i] = res[j] + [nums[i]]
    return max(res, key=len)
