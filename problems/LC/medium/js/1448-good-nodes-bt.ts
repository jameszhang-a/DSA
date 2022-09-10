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

function goodNodes(root: TreeNode | null): number {
    const dfs = (root: TreeNode | null, highest: number) => {
        if (root === null) {
            return 0;
        }

        if (root.val >= highest) {
            return dfs(root.right, root.val) + dfs(root.left, root.val) + 1;
        } else {
            return dfs(root.right, highest) + dfs(root.left, highest);
        }
    };

    return root && dfs(root, root.val);
}
