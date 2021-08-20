class Node {
  constructor(val) {
    this.val = val;
    this.left = null;
    this.right = null;
  }
}

class BST {
  constructor() {
    this.root = null;
    this.size = 0;
  }

  /**
   * Insert a number to this BST
   * @param {Number} val number to be instered
   */
  insert(val) {
    let node = new Node(val);
    if (this.root === null) {
      this.root = node;
      this.size = 1;
      return this;
    }

    this.insertHelp(this.root, node);
  }

  /**
   * Private helper method, NOT meant for accessing from outside of the class
   * @param {Node} root 
   * @param {Node} node 
   * @returns the root
   */
  insertHelp(root, node) {
    if (root === null) {
      this.size++;
      return node;
    }

    if (node.val < root.val) {
      root.left = this.insertHelp(root.left, node);
    } else if (node.val > root.val) {
      root.right = this.insertHelp(root.right, node);
    }

    return root;
  }

  /**
   * Checks if a node is the leaf
   * @param {Node} node The node to chedk on
   * @returns true if the node is a leaf node, false if not
   */
  isLeaf(node) {
    if (!node) {
      console.log("Can't check a null node");
      return null;
    }

    return node.left === null && node.right === null;
  }

  /**
   * In-Order Traversal
   * Left - Middle - Right
   */
  inOrder(root) {
    if (root === null) return;

    if (root.left) this.inOrder(root.left);
    console.log(root.val);
    if (root.right) this.inOrder(root.right);
  }

  /**
   * Pre-Order Traversal
   * Middle - Left -
   */
  preOrder(root) {
    if (root === null) return;

    console.log(root.val);
    this.preOrder(root.left);
    this.preOrder(root.right);
  }

  /**
   * Post-Order Traversal
   * Left - Right - Middle
   */
  postOrder(root) {
    if (root === null) return;

    this.postOrder(root.left);
    this.postOrder(root.right);
    console.log(root.val);
  }
}

const tree = new BST();
const node1 = new Node(5);
const node2 = new Node(3);
const node3 = new Node(8);

tree.insert(5);
tree.insert(3);
tree.insert(8);
tree.insert(2);
tree.insert(4);
tree.insert(7);
tree.insert(9);

console.log('In-Order: ');
tree.inOrder(tree.root);

console.log('Pre-Order: ');
tree.preOrder(tree.root);

console.log('Post-Order: ');
tree.postOrder(tree.root);
/**
 *      5
 *   3      8
 *  2  4   7  9
 */
