class Solution:
    def maxAlternatingSum(self, nums: list[int]) -> int:
        nums = sorted(nums, key=abs)
        mid = len(nums) // 2
        large = nums[mid:len(nums)]
        small = nums[0:mid]

        add = 0
        sub = 0
        for i in large:
            add += i**2
        for i in small:
            sub += i**2
        return add - sub
#There was a nice solution that used numpy, but this one is mine and that is the whole point.
if __name__ == '__main__':
    solution = Solution()
    result = solution.maxAlternatingSum(nums = [1,-1,2,-2,3,-3])
    print(result)