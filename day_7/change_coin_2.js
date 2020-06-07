/*
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
 */

/**
 *
 * @param amount
 * @param coins
 */
let change = function(amount, coins){
    let dp = new Array(amount+1).fill(0),
        change_left;
    dp[0] = 1;
    for (const coin of coins){
        for (let i = 0; i <= amount; i++){
            change_left = i-coin;
            dp[i] = change_left >= 0 ? dp[i] + dp[change_left]: dp[i]
        }
    }
    return dp[dp.length - 1]
}

// the below lines are for testing only and it is not part of the solution
let amount = 5;
let c = [1, 2, 5];
console.log(change(amount, c));