class Solution:
    def sumCounts(self, nums: list[int]) -> int:
        total = 0

        for start in range(len(nums)):
            unique_nums = set()

            for end in range(start, len(nums)):
                unique_nums.add(nums[end])
                total += len(unique_nums) * len(unique_nums)

        return total
#apparently there is a way to do this in O(nlog(n))
if __name__ == '__main__':
    solution = Solution()
    result = solution.sumCounts(nums = [1,2,1])
    print(result)
    assert result == 15