"""
Given an integer, write a function to determine if it is a power of two.

Example 1:

Input: 1
Output: true
Explanation: 20 = 1
"""


def isPowerOfTwo(n):
    return n != 0 and (n & (n - 1) == 0)


# the below lines are for testing only and it is not part of the solution
n1 = -100
n2 = 0
n3 = 8
n4 = 20
print(isPowerOfTwo(n1))  # False
print(isPowerOfTwo(n2))  # False
print(isPowerOfTwo(n3))  # True
print(isPowerOfTwo(n4))  # False
