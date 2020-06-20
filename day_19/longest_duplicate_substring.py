
class Solution:
    def longestDupSubstring(self, S: str) -> str:
        # O(n * log(n))
        n = len(S)
        l, r = 1, n
        nums = [ord(S[i]) - ord('a') for i in range(n)]
        longest_duplicate = ""
        # base value for the rolling hash function
        a = 26
        # modulus value for the rolling hash function to avoid overflow
        modulus = 2 ** 32
        while l <= r:
            mid = (l + r) // 2
            start = self.hash_fun(nums, a, n, modulus, mid)
            if start:
                longest_duplicate = S[start: start+mid]
                l = mid + 1
            else:
                r = mid - 1
        return longest_duplicate

    @staticmethod
    def hash_fun(nums, a, n, modulus, mid):
        h = 0
        for i in range(mid):
            h = (h * a + nums[i]) % modulus
        seen = {h}
        # const value to be used often : a**L % modulus
        aL = pow(a, mid, modulus)
        for start in range(1, n - mid + 1):
            # compute rolling hash in O(1) time
            h = (h * a - nums[start - 1] * aL + nums[start + mid - 1]) % modulus
            if h in seen:
                return start
            seen.add(h)
        return None


dup = Solution()
print(dup.longestDupSubstring("banana"))
