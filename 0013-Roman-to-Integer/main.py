class Solution:
    def romanToInt(self, s: str) -> int:
        dict = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000
        }

        answer = 0
        for i in range(len(s)):
            if  i < len(s)-1 and dict[s[i]] < dict[s[i+1]]:
                answer-=dict[s[i]]
            else:
                answer+=dict[s[i]]
        return answer

if __name__ == '__main__':
    solution = Solution()
    result = solution.romanToInt("MCMXCIV")
    print(result)