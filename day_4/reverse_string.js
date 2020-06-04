/*
Write a function that reverses a string. The input string is given as an array of characters char[].

Do not allocate extra space for another array, you must do this by modifying the input array in-place
with O(1) extra memory.

You may assume all the characters consist of printable ascii characters.



Example 1:

Input: ["h","e","l","l","o"]
Output: ["o","l","l","e","h"]
 */


let reverseString = function(s) {
    let arr_len = s.length;
    for (let i =0; i < arr_len/2; i++){
        [s[i], s[arr_len-1-i]] = [s[arr_len - 1 - i], s[i]];
    }
    // Note: the return statment is for testing only and it is not part of the leetcode solution
    return s;
}


// Note: this part is for testing only and it is not part of the leetcode solution
let input= ["h","e","l","l","o"];
console.log(reverseString(input))
