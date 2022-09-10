/**
 * Definition for a binary tree node.
 * function TreeNode(val, left, right) {
 *     this.val = (val===undefined ? 0 : val)
 *     this.left = (left===undefined ? null : left)
 *     this.right = (right===undefined ? null : right)
 * }
 */

const recur = (head, l) => {
    if (head === null) {
        return 0;
    }
    level = Math.max(l, level);

    recur(head.left, l + 1);
    recur(head.right, l + 1);
};

/**
 * @param {TreeNode} root
 * @return {number}
 */
var maxDepth = function (root) {
    let level = 0;

    recur(root, 1);
    return level;
};
