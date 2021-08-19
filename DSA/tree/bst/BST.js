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

  insert(val) {
    console.log(`inserting ${val}`);
    let node = new Node(val);
    if (this.root === null) {
      this.root = node;
      this.size = 1;
      return this;
    }

    this.insertHelp(this.root, node);
  }

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
