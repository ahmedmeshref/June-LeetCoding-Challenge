"""
You are given coins of different denominations and a total amount of money. Write a function to compute the number of
 combinations that make up that amount. You may assume that you have infinite number of each kind of coin.

Example 1:
Input: amount = 5, coins = [1, 2, 5]
Output: 4
Explanation: there are four ways to make up the amount:
5=5
5=2+2+1
5=2+1+1+1
5=1+1+1+1+1
"""


# # recursive solution, time limit error
# def change(amount, coins):
#     """
#     :param amount: Integer represents the total amount of money
#     :param coins: List of integers, each represents a coin amount
#     :return: Integer represents the number of combinations that make up that amount
#     """
#     if amount == 0:
#         return 1
#     if len(coins) == 1:
#         return int(amount % coins[0] == 0)
#     elif len(coins) == 0:
#         return 0
#     change_left = amount - coins[-1]
#     return change(amount, coins[:-1]) + change(change_left, coins) if change_left >= 0 else change(amount, coins[:-1])


# O(mn) solution, works perfectly
def change(amount, coins):
    """
    change function compute the number of combinations that make up a given amount of money using given coins
    :param amount: Integer represents the total amount of money
    :param coins: List of integers, each represents a coin amount
    :return: Integer represents the number of combinations that make up that amount
    """
    dp = [0] * (amount + 1)
    dp[0] = 1
    for coin in coins:
        for i in range(amount + 1):
            change_left = i - coin
            if change_left >= 0:
                dp[i] += dp[change_left]
    return dp[-1]


# the below lines are for testing only and it is not part of the solution
a = 500
c = [1, 2, 5]
print(change(a, c))
