from itertools import permutations


# class Solution:
#     # Time Complexity: O(n!)
#     def getPermutation(self, n, k):
#         """
#         getPermutation takes in n integer that represents the set [1,2,3,...,n] which contains a total of n! unique
#          permutations and k, return the kth permutation sequence.
#         :param n: int
#         :param k: int
#         :return: int
#         """
#         arr = [i for i in range(1, n + 1)]
#         out = ""
#         for i in list(permutations(arr))[k - 1]:
#             out += str(i)
#         return out


class Solution:
    def getPermutation(self, n, k):
        """
        getPermutation takes in n integer that represents the set [1,2,3,...,n] which contains a total of n! unique
         permutations and k, return the kth permutation sequence.
        :param n: int
        :param k: int
        :return: int
        """
        arr = list(range(1, n + 1))
        ans = ""
        for n_it in range(n, 0, -1):
            per = self.fact(n_it - 1)
            d = (k - 1) // per
            k -= d * per
            ans += str(arr[d])
            arr.pop(d)
        return ans

    @staticmethod
    def fact(last):
        ans = 1
        for i in range(2, last + 1):
            ans *= i
        return ans


n = Solution()
print(n.getPermutation(4, 9))
