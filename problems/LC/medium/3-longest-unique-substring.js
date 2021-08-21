// Requirments
// must be continuous (substring)
// must be unique

/**
 * @param {string} s
 * @return {number}
 */
var lengthOfLongestSubstring = function(s) {
  let max = 0;
  let window = [];

  for (c of s) {
    if (window.includes(c)) {
      let x = window.indexOf(c) + 1;
      window = window.slice(x);
    }
    window.push(c);
    max = Math.max(max, window.length);
  }

  return max;
};

const timeTaken = (algo, param, n) => {
  let total = 0;
  for (let i = 0; i < n; i++) {
    const t1 = performance.now();
    algo(param);
    const t2 = performance.now();

    total += t2 - t1;
  }

  console.log(`Algo time: ${total / n}`);
};

timeTaken(lengthOfLongestSubstring, 'abcabcbb', 1000);
