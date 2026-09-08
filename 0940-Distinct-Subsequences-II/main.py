class Solution:
    def distinctSubseqII(self, s: str) -> int:
        endings = {}
        for char in s:
            total_distinct_subsequences = sum(endings.values())

            new_ending_in_char = total_distinct_subsequences + 1
            endings[char] = new_ending_in_char

        print(endings)
        return sum(endings.values()) % (10**9 + 7)

if __name__ == '__main__':
    solution = Solution()
    result = solution.distinctSubseqII(s="abc")
    print(result)