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

    map(
        callback: (value: T, index: number, array: T[]) => T,
        thisArg?: any
    ): T[] {
        const res = new Array(this.length);

        for (let i = 0; i < this.length; i++) {
            const ele = this.elements[i];
            if (Object.hasOwn(this.elements, i)) {
                res[i] = callback.call(thisArg, ele, i, this.elements);
            }
        }

        return res;
    }

    filter(callback: (val: T, idx: number, array: T[]) => boolean): T[] {
        const res: T[] = [];

        for (let i = 0; i < this.length; i++) {
            const ele = this.elements[i];
            if (callback(ele, i, this.elements)) {
                res.push(ele);
            }
        }
        return res;
    }

    push(element: T) {
        this.elements = [...this.elements, element];
        this.length++;
        return element;
    }

    toString() {
        return `${this.elements}`;
    }
}

const newArr = new NewArray([0, "a", 1, "b", , "x", "y", "", "z"]);

console.log("new arr:", newArr.toString());
console.log(newArr.map((val, i) => `${val ?? ""}` + i));
console.log(
    "filter:",
    newArr.filter((x) => {
        return typeof x === "number"
            ? x % 2 === 0
            : (x ?? "").charCodeAt(0) % 2 === 0;
    })
);

const arr = [1, 2, 3, 4, 5, 6, 7, 8, "a", "b", "c"];

console.log("arr:", arr.toString());
console.log(
    "filter:",
    arr.filter((x) => {
        return typeof x === "number" ? x % 2 === 0 : x.charCodeAt(0) % 2 === 0;
    })
);
