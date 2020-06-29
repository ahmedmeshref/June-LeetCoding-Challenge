/*
Problem Description:
Given a non-empty array of integers, every element appears three times except for one, which appears exactly once.
 Find that single one.

Note:
Your algorithm should have a linear runtime complexity. Could you implement it without using extra memory?

Example 1:
Input: [2,2,3,2]
Output: 3
*/

let singleNumber = (nums) => {
    let ones = 0,
        twos = 0;

    for (const num of nums){
        ones = (ones^num) & (~twos);
        twos = (twos^num) & (~ones);
    }
    return ones;
}

// Note: the following lines are for testing only
console.log(singleNumber([5, 4, 3, 3, 3, 5, 5]))