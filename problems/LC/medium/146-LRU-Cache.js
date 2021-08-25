'use strict';

/**
 * Node class for a doubly-linked list
 */
class Node {
  constructor(key, value) {
    this.key = key;
    this.value = value;
    this.prev = null;
    this.next = null;
  }
}

class LRUCache {
  /**
    * @param {number} capacity 
    */
  constructor(capacity) {
    this.capacity = capacity;
    this.size = 0;
    this.cache = {};
    this.head = new Node(-1, 0);
    this.tail = new Node(-1, 0);
    this.head.next = this.tail;
    this.tail.prev = this.head;
  }

  /**
   * Retrievs the value given key and refreshes the key
   * @param {number} key 
   * @returns {number} value
   */
  get(key) {
    if (!(key in this.cache)) {
      //   this.print();
      return -1;
    }

    // Swap current before and after
    const curr = this.cache[key];
    const { prev: prevNode, next: nextNode } = curr;

    prevNode.next = nextNode;
    nextNode.prev = prevNode;

    // Append to the end
    this.addToEnd(curr);

    // this.print();

    // Return value of key
    return curr.value;
  }

  /**
   * @param {number} key 
   * @param {number} value 
   * @returns {void}
   */
  put(key, value) {
    // Update entry
    if (key in this.cache) {
      this.get(key);
      this.cache[key].value = value;
    } else {
      // Add new entry to cache
      const newNode = new Node(key, value);
      this.addToEnd(newNode);
      this.cache[key] = newNode;
      this.size++;
    }

    // Over capacity
    if (this.size > this.capacity) {
      this.removeHead();
    }
    // this.print();
  }

  /**
   * Adds the node to the end of the linked list
   * @param {Node} node 
   */
  addToEnd(node) {
    const { prev: prevNode } = this.tail;

    // Swap before pointers
    prevNode.next = node;
    node.prev = prevNode;

    // Swap after pointers
    node.next = this.tail;
    this.tail.prev = node;
  }

  /**
   * Removes the head node of the linked list
   */
  removeHead() {
    const { next: removeNode } = this.head;
    this.head.next = removeNode.next;
    removeNode.next.prev = this.head;

    removeNode.next = null;
    removeNode.prev = null;
    delete this.cache[removeNode.key];

    this.size--;
  }

  /*
  print() {
    let forw = this.head;
    let back = this.tail;
    const forwArr = [];
    const backArr = [];
    while (forw != null) {
      forwArr.push(forw.key);
      forw = forw.next;
    }

    while (back != null) {
      backArr.unshift(back.key);
      back = back.prev;
    }
    console.log('Forward:  ', forwArr);
    console.log('Backward: ', backArr);
    console.log(`Contains: ${Object.keys(this.cache)}`);
  }
  */
}

// const obj = new LRUCache(3);

// console.log(obj.put(1, 1));
// console.log(obj.put(2, 2));
// console.log(obj.put(3, 3));
// console.log(obj.put(4, 4));
// console.log(obj.get(4));
// console.log(obj.get(3));
// console.log(obj.get(2));
// console.log(obj.get(1));
// console.log(obj.put(5, 5));
// console.log(obj.get(1));
// console.log(obj.get(2));
// console.log(obj.get(3));
// console.log(obj.get(4));
// console.log(obj.get(5));
