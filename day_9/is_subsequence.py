from collections import defaultdict


# # solution for the follow up question
# def isSubsequence(s, t):
#     """
#     isSubsequence function takes in two strings s and t, it returns true if s is subsequence of t, false otherwise
#     :param s: string
#     :param t: string
#     :return: boolean
#     """
#     if len(s) > len(t): return False
#     if len(s) == 0: return True
#     d = defaultdict(list)
#     for ind, char in enumerate(t):
#         d[char].append(ind)
#
#     c_ind = -1
#     for char in s:
#         # check if it works without
#         if char not in d:
#             return False
#         n_ind = binary_search(d[char], c_ind)
#         if n_ind == -1:
#             return False
#         c_ind = n_ind
#     return True
#
#
# def binary_search(lst, target):
#     """
#     binary_binary_search finds and returns the index of the first element greater than target, -1 if such element
#      doesn't exist.
#     :param lst: Sorted [] of integers
#     :param target: Integer
#     :return: Integer
#     """
#     l = 0
#     r = len(lst) - 1
#     while l <= r:
#         mid = (l + r) // 2
#         if lst[mid] <= target:
#             l = mid + 1
#         else:
#             if (mid == 0) or (lst[mid - 1] <= target):
#                 return lst[mid]
#             else:
#                 r = mid - 1
#     return -1

# two pointers solution
def isSubsequence(s, t):
    i = j = 0
    while i < len(s) and j < len(t):
        if t[j] == s[i]:
            i += 1
        j += 1
    return i == len(s)


# the below lines are for testing only and it is not part of the solution
if __name__ == "__main__":
    sub = "abc"
    string = "ahbgdc"
    print(isSubsequence(sub, string))
