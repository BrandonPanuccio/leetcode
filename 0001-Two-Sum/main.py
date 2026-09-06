class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        seen = {}
        for i in range(len(nums)):
            compliment = target - nums[i]
            if compliment in seen:
                return [seen[compliment], i]
            seen[nums[i]] = i

        return []

if __name__ == '__main__':
    solution = Solution();
    result = solution.twoSum(nums = [3,2,4], target = 6)
    print(result)