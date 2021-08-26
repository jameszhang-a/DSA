class Node {
  constructor(val, prio) {
    this.val = val;
    this.priority = prio;
  }
}

class PriorityQueue {
  constructor() {
    this.heap = [];
  }

  /**
   * Transforms an array into a min-heap
   * @param {Array} arr An array in any order
   * @returns this.heap: a heap
   */
  buildHeap(arr) {
    // Edge case
    if (arr.length === 1 || arr.length === 0) return arr;

    // Calculates the last parent node, and begin heapify
    const { idx: mid } = this.getParent(arr.length - 1);

    // Travels reverse-level-order until the root
    for (let i = mid; i >= 0; i--) {
      this.heapify(arr, i);
    }
  }

  /**
   * Recurrsive function to heapify a single value to its rightful place
   * @param {Array} arr the array to be heapified
   * @param {Number} idx index of the node to be heapified
   */
  heapify(arr, idx) {
    // Compare with two child nodes
    const l = idx * 2 + 1;
    const r = idx * 2 + 2;

    // Find the min between idx, left, and right
    let min = idx;
    if (l < arr.length && arr[min].priority > arr[l].priority) min = l;
    if (r < arr.length && arr[min].priority > arr[r].priority) min = r;

    // Stops when the node is smallest out of the children
    while (arr[idx].priority > arr[min].priority) {
      // Swap the two values
      const temp = arr[idx];
      arr[idx] = arr[min];
      arr[min] = temp;

      // Heapify the new, lower index
      this.heapify(arr, min);
    }
  }

  /**
   * enqueues a value at the end of the heap, then bubbles into the right order
   * @param {Number} num Data to be enqueued
   */
  enqueue(val, prio) {
    // Construct new node form input
    const node = new Node(val, prio);
    if (this.heap.length === 0) {
      this.heap.push(node);
      return;
    }

    // Checks for dups
    if (this.heap.some((node) => node.val === val)) {
      console.log(`Cannot enqueue the same item: '${val}'`);
      return null;
    }

    // Start with the new node at the end
    this.heap.push(node);

    // Current size is the location of a new enqueue
    let curr = this.heap.length - 1;

    // bubble up if has parent, and the parent is larger
    while (
      this.getParent(curr).idx >= 0 &&
      prio < this.getParent(curr).parent.priority
    ) {
      // Swap nodes between the current and the parent
      const { idx, parent } = this.getParent(curr);
      this.heap[idx] = node;
      this.heap[curr] = parent;

      // Update new location of the new node
      curr = idx;
    }
  }

  /**
   * Returns the object containing info about the parent of the child
   * Math.floor((idx - 1) / 2)
   * @param {Number} idx Index of the child
   * @returns idx: the index of the parent
   * @returns parent: the value of the parent
   */
  getParent(idx) {
    const parentIdx = Math.floor((idx - 1) / 2);
    const parent = this.heap[parentIdx];
    return {
      idx    : parentIdx,
      parent
    };
  }

  /**
   * Returns the left child and its index of the parent
   * @param {Number} idx index of the parent
   */
  getLeft(idx) {
    const childIdx = 2 * idx + 1;
    const child = this.heap[childIdx];
    return {
      idx   : childIdx,
      child
    };
  }

  /**
   * Returns the right child and its index of the parent
   * @param {Number} idx index of the parent
   */
  getRight(idx) {
    const childIdx = 2 * idx + 2;
    const child = this.heap[childIdx];
    return {
      idx   : childIdx,
      child
    };
  }

  /**
   * Dequeues and returns the min value of the heap
   * @returns The minumum value of the heap
   */
  dequeue() {
    // If empty
    if (this.heap.length === 0) {
      console.log('Empty heap');
      return null;
    }

    // If only one element
    if (this.heap.length === 1) return this.heap.pop().val;

    // Swap last element to the top
    const min = this.heap[0];
    const end = this.heap.pop();
    this.heap[0] = end;

    // Heapify from the top
    this.heapify(this.heap, 0);

    return min.val;
  }
}

// Tests
// const heap = new MinHeap([ 5, 14, 23, 32, 41, 87, 90, 50, 64, 53 ]);
// console.log(heap);

// const test = new MinHeap([ 4 ]);
// console.log(test);

// console.log(test.heap);

const arr = [ 5, 11, 9, 20, 2, 19, 3, 15, 12, 1 ];

const queue = new PriorityQueue();
console.log(queue);

const one = new Node(5, 'a');
const two = new Node(11, 'b');
const three = new Node(9, 'c');
const four = new Node(20, 'd');
const five = new Node(2, 'e');

queue.enqueue('a', 5);
console.log(queue);

queue.enqueue('b', 11);
console.log(queue);

queue.enqueue('c', 9);
console.log(queue);

queue.enqueue('e', 2);
console.log(queue);

queue.enqueue('e', 55);

queue.dequeue();
console.log(queue);

queue.dequeue();
console.log(queue);
