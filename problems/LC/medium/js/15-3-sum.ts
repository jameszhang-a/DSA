/**
Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]]
such that i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0.

Notice that the solution set must not contain duplicate triplets.

Example 1:
Input: nums = [-1,0,1,2,-1,-4]
Output: [[-1,-1,2],[-1,0,1]]
Explanation:
nums[0] + nums[1] + nums[2] = (-1) + 0 + 1 = 0.
nums[1] + nums[2] + nums[4] = 0 + 1 + (-1) = 0.
nums[0] + nums[3] + nums[4] = (-1) + 2 + (-1) = 0.
The distinct triplets are [-1,0,1] and [-1,-1,2].
Notice that the order of the output and the order of the triplets does not matter.

Example 2:
Input: nums = [0,1,1]
Output: []
Explanation: The only possible triplet does not sum up to 0.

Example 3:
Input: nums = [0,0,0]
Output: [[0,0,0]]
Explanation: The only possible triplet sums up to 0.

Constraints:
3 <= nums.length <= 3000
-105 <= nums[i] <= 105
 */

const threeSum = (nums: number[]): number[][] => {
    const result: number[][] = [];

    nums.sort((a, b) => a - b);

    // fix 1 number, then run 2 sum
    for (let i = 0; i < nums.length - 1; i++) {
        // skips duplicate
        if (i > 0 && nums[i] === nums[i - 1]) continue;

        let l = i + 1,
            r = nums.length - 1,
            goal = nums[i];

        while (l < r) {
            const sum = nums[l] + nums[r];

            if (sum < -goal) {
                l += 1;
            } else if (sum > -goal) {
                r -= 1;
            } else {
                result.push([goal, nums[l], nums[r]]);
                l += 1;
                r -= 1;

                // skips duplicate
                while (nums[l] === nums[l - 1]) l++;
            }
        }
    }

    return result;
};

const test = () => {
    const input: [number[]][] = [
        [[-1, 0, 1, 2, -1, -4]],
        [[0, 1, 1]],
        [[0, 0, 0]],
    ];
    const output = [
        [
            [-1, -1, 2],
            [-1, 0, 1],
        ],
        [],
        [[0, 0, 0]],
    ];
    for (let i = 0; i < input.length; i++) {
        const result = threeSum(...input[i]);
        const correct = JSON.stringify(result) === JSON.stringify(output[i]);
        console.log(correct);
        if (!correct) {
            console.log("expected:", output[i]);
            console.log("actual:", result);
        }
        console.log();
    }
};

test();
export {};
