class NewArray<T> {
    public elements: T[];
    public length: number = 0;

    constructor(elements: T[]) {
        this.elements = elements;
        this.length = elements.length;
    }

    first() {
        return this.elements[0];
    }

    map<T>(callback: (value: any, index: number, array: any[]) => any): T[] {
        const res: T[] = [];
        for (let i = 0; i < this.length; i++) {
            res.push(callback(this.elements[i], i, this.elements));
        }
        return res;
    }

    push(element: T) {
        this.elements = [...this.elements, element];
        this.length++;
        return element;
    }
}

const arr = new NewArray([0, "a", 1, "b", , "x", "y", "", "z"]);

const f = (val: number, idx: number) => {
    return val + idx;
};

console.log(arr.map(f));
console.log(arr.length);

console.log(arr);
arr.push("new element");
console.log(arr.elements);

const a = [1, 2, 3];

a.map(f);
