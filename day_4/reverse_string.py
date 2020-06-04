"""
Write a function that reverses a string. The input string is given as an array of characters char[].

Do not allocate extra space for another array, you must do this by modifying the input array in-place
with O(1) extra memory.

You may assume all the characters consist of printable ascii characters.



Example 1:

Input: ["h","e","l","l","o"]
Output: ["o","l","l","e","h"]
"""


def reverseString(s):
    """
    reverseString reverses the string in s list in place
    :param s: list of characters
    :return: list reversed
    """
    for i in range(len(s) // 2):
        s[i], s[-i - 1] = s[-i - 1], s[i]
    return s


# Note: this is not part of the solution, it is for testing only
n = ["h", "e", "l", "l", "o"]
print(reverseString(n))
