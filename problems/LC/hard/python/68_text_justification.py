"""
Given an array of strings words and a width maxWidth, format the text such that each line
has exactly maxWidth characters and is fully (left and right) justified.

You should pack your words in a greedy approach; that is, pack as many words as you can
in each line. Pad extra spaces ' ' when necessary so that each line has exactly maxWidth
characters.

Extra spaces between words should be distributed as evenly as possible. If the number
of spaces on a line does not divide evenly between words, the empty slots on the left
will be assigned more spaces than the slots on the right.

For the last line of text, it should be left-justified, and no extra space is inserted
between words.

Note:
A word is defined as a character sequence consisting of non-space characters only.
Each word's length is guaranteed to be greater than 0 and not exceed maxWidth.
The input array words contains at least one word.


Example 1:
Input: words = ["This", "is", "an", "example", "of", "text", "justification."], maxWidth = 16
Output:
[
   "This    is    an",
   "example  of text",
   "justification.  "
]

Example 2:
Input: words = ["What","must","be","acknowledgment","shall","be"], maxWidth = 16
Output:
[
  "What   must   be",
  "acknowledgment  ",
  "shall be        "
]
Explanation: Note that the last line is "shall be    " instead of "shall     be", because the last line must be left-justified instead of fully-justified.
Note that the second line is also left-justified because it contains only one word.

Example 3:
Input: words = ["Science","is","what","we","understand","well","enough","to","explain","to","a","computer.","Art","is","everything","else","we","do"], maxWidth = 20
Output:
[
  "Science  is  what we",
  "understand      well",
  "enough to explain to",
  "a  computer.  Art is",
  "everything  else  we",
  "do                  "
]
"""


from typing import List


class Solution:
    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:
        """
        case: can add new word
        - add new word
        - increase j pointer until can't add word
        - calculate how many spaces needed
        - justify each word

        """
        res = []
        i, j = 0, 1

        while j < len(words) or i < len(words):
            if j >= len(words):
                toAdd = words[i].ljust(maxWidth)
            else:
                lineLen = len(words[i])
                line = [words[i]]
                numWords = 1

                # chars of each line, current line + new word + min spaces
                while j < len(words) and lineLen + len(words[j]) + (numWords - 1) < maxWidth:
                    lineLen += len(words[j])
                    line.append(words[j])
                    numWords += 1
                    j += 1

                # can't add new words, calculate now many spaces left
                leftOverSpaces = maxWidth - lineLen

                # 2 cases, if there are multiple words, or if only 1 word in line
                if numWords == 1 or j >= len(words):
                    toAdd = " ".join(line).ljust(maxWidth)
                else:
                    # using mod to find common: spaces between each word, and extra: how many spaces
                    # in the front need an extra space
                    common, extra = divmod(leftOverSpaces, numWords - 1)
                    toAdd = ""
                    for i in range(numWords):
                        if not extra:
                            break
                        line[i] += " "
                        extra -= 1

                    toAdd = (common * " ").join(line)

            res.append(toAdd)

            i = j
            j += 1

        return res

    def test(self, inputs, outputs):
        for i, input in enumerate(inputs):
            if (out := self.fullJustify(*input)) != outputs[i]:
                print(f"{i} failed")
                print(f"Output:	 {out}")
                print(f"Correct: {outputs[i]}")
                print("")
                continue

            print(f"{i} pass")


input = [
    # [["This", "is", "an", "example", "of", "text", "justification."], 16],
    # [["What", "must", "be", "acknowledgment", "shall", "be"], 16],
    [
        [
            "Science",
            "is",
            "what",
            "we",
            "understand",
            "well",
            "enough",
            "to",
            "explain",
            "to",
            "a",
            "computer.",
            "Art",
            "is",
            "everything",
            "else",
            "we",
            "do",
        ],
        20,
    ],
]
expected = [
    # [
    #     "This    is    an",
    #     "example  of text",
    #     "justification.  ",
    # ],
    # [
    #     "What   must   be",
    #     "acknowledgment  ",
    #     "shall be        ",
    # ],
    [
        "Science  is  what we",
        "understand      well",
        "enough to explain to",
        "a  computer.  Art is",
        "everything  else  we",
        "do                  ",
    ],
]


sol = Solution()
sol.test(input, expected)
