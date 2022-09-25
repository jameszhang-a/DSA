/**
 * Problem
 * input: arr: [1,2,3,4,5,6], n: 3
 * output: 15
 *
 * Given an array and a number,
 * find the max sum of n concscutive numbers in the array
 */

/**
 * Brute force solution
 *
 * For each element in arr, sum the next n elements
 * O(n*m)
 */
const findMaxSum = (arr, n) => {
    let max = 0;

    // Edge case
    if (n > arr.length) return null;
    else if (n === 0) return 0;

    // Goes through each element of the array up until [:-n]
    for (let i = 0; i < arr.length - n + 1; i++) {
        let temp = 0;
        for (let j = 0; j < n; j++) {
            temp += arr[i + j];
        }

        // Replace max if temp is larger
        max = temp > max ? temp : max;
    }
    return max;
};

/**
 * Sliding-window solution
 *
 * Start with first n sum
 * Loop and sub first, add last
 *
 * O(n)
 */
const betterFindMaxSum = (arr, n) => {
    let sum = arr.slice(0, n).reduce((prev, cur) => prev + cur, 0);
    let res = sum;

    for (let i = n; i < arr.length; i++) {
        sum = -arr[i - n] + arr[i] + sum;
        res = Math.max(res, sum);
    }
    return res;
};

console.log(betterFindMaxSum([1, 2, 4, 2, 8, 1, 5], 2)); // 10
