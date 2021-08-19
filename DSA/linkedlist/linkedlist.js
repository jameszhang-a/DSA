import Node from './node.js';

class linkedList {
  constructor(head) {
    this.head = head;
    this.length = 1;
  }

  /**
   * Adds a new block to the end of the linked list
   * @param {any} val Any value for the new block
   */
  push(val) {
    const newNode = new Node(val);
    let temp = this.head;

    // Get to the last node
    while (temp.next !== null) {
      temp = temp.next;
    }

    // push new node and incriment length
    temp.next = newNode;
    this.length++;
  }

  /**
   * Reverses the linked list in place iteratively
   */
  reverse() {
    let temp = this.head;
    let curr;
    let pre = null;

    while (temp) {
      curr = temp.next;
      temp.next = pre;
      pre = temp;
      temp = curr;
    }

    this.head = pre;
  }

  /**
   * prints the linked list in order for debug purposes
   */
  printList() {
    let temp = this.head;
    console.log('Length: ', this.length);
    while (temp !== null) {
      console.log(temp.val);
      temp = temp.next;
    }
  }
}

const head = new Node(5);
const list = new linkedList(head);
list.push(4);
list.push('a');
list.push(99);
list.push('abc');

list.printList();

list.reverse();

list.printList();
