/*
Given an integer, write a function to determine if it is a power of two.

Example 1:

Input: 1
Output: true
Explanation: 20 = 1
*/

let isPowerOfTwo = function (n) {
    return n <= 0 ? false : (n & (n - 1)) === 0;
}

// the below lines are for testing only and it is not part of the solution
let n1 = -100,
    n2 = 0,
    n3 = 8,
    n4 = 20;
console.log(isPowerOfTwo(n1));
console.log(isPowerOfTwo(n2));
console.log(isPowerOfTwo(n3));
console.log(isPowerOfTwo(n4));