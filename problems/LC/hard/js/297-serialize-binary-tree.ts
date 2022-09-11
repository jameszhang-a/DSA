/*
Serialization is the process of converting a data structure or object into a sequence of bits so that it can be stored in a file or memory buffer,
or transmitted across a network connection link to be reconstructed later in the same or another computer environment.

Design an algorithm to serialize and deserialize a binary tree. There is no restriction on how your serialization/deserialization algorithm should
work. You just need to ensure that a binary tree can be serialized to a string and this string can be deserialized to the original tree structure.

Clarification: The input/output format is the same as how LeetCode serializes a binary tree. You do not necessarily need to follow this format,
so please be creative and come up with different approaches yourself.



Example 1:
Input: root = [1,2,3,null,null,4,5]
Output: [1,2,3,null,null,4,5]

Example 2:
Input: root = []
Output: []
*/

// Definition for a binary tree node.
class TreeNode {
    val: number;
    left: TreeNode | null;
    right: TreeNode | null;
    constructor(val?: number, left?: TreeNode | null, right?: TreeNode | null) {
        this.val = val === undefined ? 0 : val;
        this.left = left === undefined ? null : left;
        this.right = right === undefined ? null : right;
    }
}

/*
 * Encodes a tree to a single string.
 */
function serialize(root: TreeNode | null): string {
    let res: (string | number)[] = [];
    const dfs = (root: TreeNode | null) => {
        if (!root) {
            res.push("x");
            return;
        }

        res.push(root.val);

        dfs(root.left);
        dfs(root.right);
    };

    dfs(root);
    return res.join(",");
}

/*
 * Decodes your encoded data to tree.
 */
function deserialize(data: string): any {
    const dfs = (arr: String[]): TreeNode | null => {
        // if (arr.length < 1) return null;

        let val = arr.shift();
        if (val === "x") {
            return null;
        }

        const num = parseInt(val as string);

        const node = new TreeNode(num);
        node.left = dfs(arr);
        node.right = dfs(arr);
        return node;
    };

    const str = data.split(",");
    console.log(str);
    return dfs(str);
}

/**
 * Your functions will be called as such:
 * deserialize(serialize(root));
 */

console.log(
    deserialize(
        serialize(
            new TreeNode(
                1,
                new TreeNode(2),
                new TreeNode(3, new TreeNode(4), new TreeNode(5))
            )
        )
    )
);

