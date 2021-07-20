class Solution:
    def fizzBuzz(self, n: int):
        result = list()
        for num in range(1, n+1):
            if num % 5 == 0 and num % 3 == 0:
                result.append("FizzBuzz")
            elif num % 3 == 0:
                result.append("Fizz")
            elif num % 5 == 0:
                result.append("Buzz")
            else:
                result.append(str(num))
        return result


test = Solution()
print(test.fizzBuzz(5))
