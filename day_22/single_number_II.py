"""
Problem Description:
Given a non-empty array of integers, every element appears three times except for one, which appears exactly once.
 Find that single one.

Note:
Your algorithm should have a linear runtime complexity. Could you implement it without using extra memory?

Example 1:
Input: [2,2,3,2]
Output: 3
"""

from collections import Counter


#
# def singleNumber(nums):
#     """
#     Time: O(n), Space: O(n)
#     :param nums: [int]
#     :return: int
#     """
#     c = Counter(nums)
#     for k, v in c.items():
#         if v == 1:
#             return k
#     return None


# solution with no extra space using ones and twos complement
def singleNumber(nums):
    """
    Time: O(n), Space: O(1)
    :param nums: [int]
    :return: int
    """
    ones = 0
    twos = 0
    for num in nums:
        # ones = (ones XOR num) AND (COMPLEMENT twos)
        ones = (ones ^ num) & (~twos)
        twos = (twos ^ num) & (~ones)
    return ones


# the following lines are for testing only
print(singleNumber([2, 2, 1, 4, 4, 2, 4]))