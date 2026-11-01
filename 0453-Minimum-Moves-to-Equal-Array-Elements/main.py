class Solution:
    def minMoves(self, nums: list[int]) -> int:
        return sum(nums) - len(nums) * min(nums)

if __name__ == '__main__':
    solution = Solution()
    result = solution.minMoves(nums = [1,2,3])
    print(result)