class Node {
  constructor(val) {
    this.val = val;
    this.left = null;
    this.right = null;
  }
}

class BST {
  COUNT = 5;

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

    // If the tree is empty
    if (this.root === null) {
      this.root = node;
      this.size = 1;
      return this;
    }

    if (this.contains(this.root, val)) {
      console.log("Can't insert a dup!");
      return null;
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

  contains(val) {
    let node = new Node(val);

    if (this.root === null) {
      console.log('Cant search empty tree');
      return null;
    }

    return this.containsHelp(this.root, node);
  }

  containsHelp(root, node) {
    // Can't find the value
    if (root === null) return false;

    // Found the value
    if (root.val === node.val) return true;

    if (node.val < root.val) return this.containsHelp(root.left, node);
    else if (node.val > root.val) return this.containsHelp(root.right, node);
  }

  findMin() {
    if (this.root === null) {
      console.log('Empty tree');
      return null;
    }
    if (this.isLeaf(this.root)) return this.root.val;

    return this.findMinHelp(this.root);
  }

  findMinHelp(node) {
    if (node.left === null) return node.val;

    return this.findMinHelp(node.left);
  }

  findMax() {
    if (this.root === null) {
      console.log('Empty Tree');
      return null;
    }
    if (this.isLeaf(this.root)) return this.root.val;

    return this.findMaxHelp(this.root);
  }

  findMaxHelp(node) {
    if (node.right === null) return node.val;

    return this.findMaxHelp(node.right);
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

  // Wrapper over print2DUtil()
  print2D(root) {
    // Pass initial space count as 0
    this.print2DUtil(root, 0);
  }

  // Function to print binary tree in 2D
  // It does reverse inorder traversal
  print2DUtil(root, space) {
    // Base case
    if (root == null) return;

    // Increase distance between levels
    space += this.COUNT;

    // Process right child first
    this.print2DUtil(root.right, space);

    // Print current node after space count
    let str = '';
    str += '\n';
    for (let i = this.COUNT; i < space; i++) str += '  ';
    str = str + root.val + '\n';
    console.log(str);
    // Process left child
    this.print2DUtil(root.left, space);
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

/**
 *      5
 *   3      8
 *  2  4   7  9
 */

console.log(tree.contains(-1));
tree.print2D(tree.root);

// console.log('In-Order: ');
// tree.inOrder(tree.root);

// console.log('Pre-Order: ');
// tree.preOrder(tree.root);

// console.log('Post-Order: ');
// tree.postOrder(tree.root);

console.log(`Min ${tree.findMin()}`);
console.log(`Max ${tree.findMax()}`);
