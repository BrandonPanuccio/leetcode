class Solution:
    def totalNumbers(self, digits: list[int]) -> int:
        counts = [0] * 10

        for digit in digits:
            counts[digit] += 1
        
        output = 0

        for num in range(100, 1000, 2):
            needed = [0] * 10
            hundreds = num // 100
            tens = (num // 10) % 10
            ones = num % 10  

            needed[hundreds] += 1
            needed[tens] += 1
            needed[ones] += 1

            pass_all_digits = True

            for i in range(10):
                if needed[i] > counts[i]:
                    pass_all_digits = False
                    break

            if pass_all_digits:
                output += 1

        return output

if __name__ == '__main__':
    solution = Solution()
    result = solution.totalNumbers(digits=[1,2,3,4])
    print(result)